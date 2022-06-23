from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

#@frappe.whitelist(allow_guest=True)
def calculate_gross_salary(self,method):
        if self.ind_company_accommodation=="Yes":
            self.ind_food_allowance=300
#        else:
#            self.ind_food_allowance=0

        if self.ind_housing_allowance_provided=="Yes":
            self.ind_hra=self.base*0.25
#        else:
#            self.ind_hra=0

        if self.ind_transportation_allowance_provided=="Yes":
            if self.base<15001:
                self.ind_transport_allowance=self.base*0.10
            else:
                self.ind_transport_allowance=1500
#        else:
#            self.ind_transport_allowance=0
            
        self.ind_gross_salary=self.base+self.ind_food_allowance+self.ind_hra+self.ind_transport_allowance+self.ind_mobile_allowance+self.ind_hardship_allowance+self.ind_school_fees_allowance
#            frappe.throw(_("Test"))
