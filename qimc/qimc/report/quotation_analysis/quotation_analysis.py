# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data()
	return columns, data

def get_columns():
	return [
		_("Quotation") + ":Link/Quotation:150",
		_("Customer") + ":Link/Customer:300",
		_("Item Name") + ":Link/Item:150",
		_("UOM") + ":Data:100",
		_("Qty") + ":Float:100",
		_("Rate") + ":Currency:100",
		_("Amount") + ":Currency:150",
	]

def get_data():
	return frappe.db.sql("""
	select
	A.name,
    A.customer_name,
    B.item_name,
	B.uom,
	B.qty,
	B.rate,
	B.amount

	FROM
	`tabQuotation` as A,
    `tabQuotation Item` as B

    ORDER BY A.name ASC
	""")
