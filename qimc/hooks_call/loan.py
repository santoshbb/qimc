from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, get_datetime, getdate, date_diff, nowdate

#@frappe.whitelist(allow_guest=True)
def duplicate_loan(self, method):
        last_transaction = frappe.get_list("Loan",
            fields=["applicant", "status"],
            filters = {
                "applicant": self.applicant,
                "ind_loan_repayment_status" : "Repayment not Complete",
                "docstatus" : 1
#                "name": ("!=", self.name)
            })
        
        if (len(last_transaction))>0:
            frappe.throw("Loan Repayment Status should be Repayment Complete")
#            msg = _("Applicant {0} {1} has not been recorded as returned since {2}")
#            self.ind_loan_repayment_status_test=last_transaction
#       if self.loan_type=="Personal Loan":
#            for d in self.repayment_schedule:
#                if d.payment<=get_today():
#                    if d.balance_loan_amount=="0":
#                        frappe.throw(("You have not cleared previous loan"))
#                        frappe.throw(("You have not cleared previous loan", self.posting_date))

