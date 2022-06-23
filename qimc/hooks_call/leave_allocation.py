from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate, rounded, date_diff, getdate,getdate, add_months, get_first_day, add_days
from erpnext.hr.utils import get_employee_leave_policy, check_frequency_hit, create_additional_leave_ledger_entry


#@frappe.whitelist(allow_guest=True)
def calculate_days_to_allocate(self,method):
    self.from_date=frappe.defaults.get_user_default("year_start_date")
    self.to_date=frappe.defaults.get_user_default("year_end_date")
    if date_diff(self.from_date, self.ind_date_of_joining)<0:
        self.ind_days_to_allocate = date_diff(self.to_date, self.ind_date_of_joining)
        self.new_leaves_allocated = rounded(self.ind_days_to_allocate * self.ind_max_leaves_allowed / 365)
    else:
        self.new_leaves_allocated=self.ind_max_leaves_allowed

def allocate_earned_leaves_to_employees_who_joined_last_month(self,method):
	'''Allocate earned leaves to Employees who joined last month'''
	print("allocate_earned_leaves_to_employees_who_joined_last_month")
	e_leave_types = frappe.get_all("Leave Type",
		fields=["name", "max_leaves_allowed", "earned_leave_frequency", "rounding"],
		filters={'is_earned_leave' : 1})
	today = getdate()
	divide_by_frequency = {"Yearly": 1, "Half-Yearly": 6, "Quarterly": 4, "Monthly": 12}
	divide_by_frequency_per_day = {"Yearly": 365, "Half-Yearly": 183, "Quarterly": 90, "Monthly": 30}

	for e_leave_type in e_leave_types:
		leave_allocations = frappe.db.sql("""select name, employee, from_date, to_date from `tabLeave Allocation` where %s
			between from_date and to_date and docstatus=1 and leave_type=%s""", (today, e_leave_type.name), as_dict=1)
		for allocation in leave_allocations:
			employee_date_of_joining = frappe.db.get_value("Employee", allocation.employee, "date_of_joining")

			first_date_of_last_month = get_first_day(add_months(today, -1))
			if employee_date_of_joining < today and employee_date_of_joining >= first_date_of_last_month:
				print("true")
				working_days = date_diff(add_days(today, -1), employee_date_of_joining)
				print (working_days)
				leave_policy = get_employee_leave_policy(allocation.employee)
				if not leave_policy:
					continue
				if not e_leave_type.earned_leave_frequency == "Monthly":
					if not check_frequency_hit(allocation.from_date, today, e_leave_type.earned_leave_frequency):
						continue
				annual_allocation = frappe.db.get_value("Leave Policy Detail", filters={
					'parent': leave_policy.name,
					'leave_type': e_leave_type.name
				}, fieldname=['annual_allocation'])
				if annual_allocation:
					earned_leaves = flt(annual_allocation) / divide_by_frequency[e_leave_type.earned_leave_frequency]
					custom_earned_leaves = flt(annual_allocation * working_days) / divide_by_frequency_per_day[e_leave_type.earned_leave_frequency]
					if e_leave_type.rounding == "0.5":
						earned_leaves = round(earned_leaves * 2) / 2
					else:
						earned_leaves = round(earned_leaves)

					if e_leave_type.rounding == "0.5":
						custom_earned_leaves = round(custom_earned_leaves * 2) / 2
					else:
						custom_earned_leaves = round(custom_earned_leaves)


					allocation = frappe.get_doc('Leave Allocation', allocation.name)
					new_allocation = flt(allocation.total_leaves_allocated) - flt(earned_leaves) + flt(custom_earned_leaves)

					if new_allocation > e_leave_type.max_leaves_allowed and e_leave_type.max_leaves_allowed > 0:
						new_allocation = e_leave_type.max_leaves_allowed

					if new_allocation == allocation.total_leaves_allocated:
						continue
					
					allocation.db_set("total_leaves_allocated", new_allocation, update_modified=False)
					frappe.db.sql("""DELETE
									 FROM `tabLeave Ledger Entry`
									 WHERE
									 	transaction_type = 'Leave Allocation'
									 	AND leave_type = %s""")
