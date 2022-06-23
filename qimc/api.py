from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.utils import floor, flt, today, cint, cstr


@frappe.whitelist()
def calculate_deductible_hours(self,method):
    deductible_hours = 0
    if self.status == "Present":
        if flt(self.working_hours) < 7.5 and flt(self.working_hours) > 5:
            self.ind_deductible_hours = 7.5 - self.working_hours

@frappe.whitelist()
def validate_approved_hours(self,method):
    if self.ind_approved_hours>self.ind_deductible_hours:
        frappe.throw(_("Approved hours cannot be more than deducted hours"))

@frappe.whitelist()
def calculate_deductible_hours_salary_slip(self,method):
    attendance = frappe.db.sql("""SELECT sum(ind_deductible_hours) AS 'ind_deductible_hours',
    sum(ind_approved_hours) AS 'ind_approved_hours'
    
FROM `tabAttendance`
WHERE employee=%s
  AND attendance_date BETWEEN %s AND %s""",(self.employee,self.start_date,self.end_date),as_dict=1)
    if len(attendance) >= 1:
        self.ind_hours = attendance[0].ind_deductible_hours
        self.ind_approved_hours = attendance[0].ind_approved_hours
#        if (self.ind_approved_hours<=self.ind_hours):
#        else :
#            self.ind_approved_hours=self.ind_hours
