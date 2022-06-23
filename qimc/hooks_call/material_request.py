from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

#@frappe.whitelist(allow_guest=True)
def sales_user_validation(self,method):
    self.ind_employee=frappe.session.user
#    if (self.ind_department!="Sales - QIMC"):
    for d in self.get("items"):
            if (d.ind_item_group=="Finished Goods"):
                self.material_request_type="Material Transfer"
#                self.ind_test=frappe.get_roles(frappe.session.user)
#                frappe.throw(_("You are allowed only for Finished Goods"))
#            if (self.material_request_type=="Material Transfer"):      
#        if (frappe.get_roles(frappe.session.user)!="Sales User"):
               
