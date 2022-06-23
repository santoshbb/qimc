# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters)
	data=get_data(filters)
#        conditions=get_conditions(filters)
	return columns, data

def get_columns(filters):
 if filters.get("details"):
  if filters.get("details")=="More Details":
    return [

      _("Item Code") + ":Link/Item:180",
      _("Item Name") + ":Data:270",
      _("Item Group") + ":Data:130",
      _("UOM") + ":Data:100",
      _("Weight (Kg)") + ":Data:100",
      _("Income Account") + ":Data:140",
      _("Income Cost Center") + ":Data:140",
      _("Expense Account") + ":Data:140",
      _("Expense Cost Center") + ":Data:140",
      _("Created By") + ":Data:180"
   ]
  else:
   return [
    _("Item Group") + ":Data:200",
    _("Abbreviation") + ":Data:120",
    _("Total Item Masters") + ":Float:150"
   ]

def get_data(filters):
 if filters.get("details"):
  if filters.get("details")=="More Details":
    if filters.get("item_group"):
     item_group=filters.get("item_group")
     return frappe.db.sql("""
      SELECT

      A.name,
      A.item_name,
      A.item_group,
      A.stock_uom,
      A.weight_per_unit,
      B.income_account,
      B.selling_cost_center,
      B.expense_account,
      B.buying_cost_center,
      A.owner
  
      FROM
      `tabItem` AS A,
      `tabItem Default` AS B
  
      WHERE
      A.item_group = '%s'
      AND A.name = B.parent
      ORDER BY A.item_code DESC """ %(item_group), as_list=1)

    else:
     return frappe.db.sql("""
      SELECT
      
      A.name,
      A.item_name,
      A.item_group,
      A.stock_uom,
      A.weight_per_unit,
      B.income_account,
      B.selling_cost_center,
      B.expense_account,
      B.buying_cost_center,
      A.owner
  
      FROM
      `tabItem` AS A,
      `tabItem Default` AS B
      WHERE
      A.name = B.parent

      ORDER BY A.item_code DESC """ ) 
  else:
    return frappe.db.sql("""
    SELECT DISTINCT
    A.item_group,
    B.naming_series_for_item,
    count(A.name)
    
    FROM
    `tabItem` AS A,
    `tabItem Group` AS B
    WHERE
    A.item_group=B.name
    GROUP BY A.item_group  """ )