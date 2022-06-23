from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

#@frappe.whitelist(allow_guest=True)
def validate_purpose_manufacture(self,method):
    if self.job_card:
        if (self.purpose != "Material Transfer for Manufacture" or self.purpose != "Manufacture"):
            frappe.throw(_("Purpose should be 1.Manufacture 2.Material Transfer for Manufacture"))
               