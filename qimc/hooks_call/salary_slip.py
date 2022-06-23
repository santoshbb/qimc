from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

#@frappe.whitelist(allow_guest=True)
def validate_calculate_end_date(self,method):
#    self.total_working_days=30
#    self.payment_days=self.total_working_days-self.leave_without_pay
    if ((self.ind_leave_without_pay_25_percent + self.ind_sl100) > self.leave_without_pay):
        frappe.throw(_("Sick Leave 100 pay and 75 pay should be less than Total Leave"))

#    if (self.payroll_frequency=="Monthly" and self.total_working_days!=30):
#         frappe.throw(_("Working Days should be 30, Please change End Date"))
