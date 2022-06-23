# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters)
	return columns, data

def get_columns():
	return [

		_("Job Card") + ":Link/Job Card:100",
		_("Stage") + ":Int:70",
		_("Operation") + ":Data:130",
		_("For Qty") + ":Float:90",
		_("Transfered Qty") + ":Float:110",
		_("Completed Qty") + ":Float:110",
		_("Rejection") + ":Float:80",
		_("Accepted Qty") + ":Float:110",
		_("Time Takes(min)") + ":Float:120",
		_("JC Status") + ":Data:90",
		_("WO Status") + ":Data:100"
	]

def get_data(filters):
	
	if filters.get("work_order"):
		work_order=filters.get("work_order")
		if filters.get("details")=="Summary":

				return frappe.db.sql("""
					select
					A.name,
					A.ind_stage,
					A.operation,
					sum(A.for_Quantity),
					sum(A.transferred_qty),
					sum(A.total_completed_qty),
					sum(A.ind_rejection),
					IF(A.status="Completed", sum(A.total_completed_qty)-sum(A.ind_rejection),0),
					sum(A.total_time_in_mins),
					IF(A.docstatus="2","Cancelled",A.status),
					B.status

					FROM
					`tabJob Card` as A,
					`tabWork Order` as B

					WHERE
					A.work_order=B.name
					&& A.docstatus!="2"
					&& A.work_order = '%s'

					GROUP BY A.operation
					ORDER BY A.ind_stage ASC """ %(work_order), as_list=1)

		if filters.get("details")=="More Details":
							return frappe.db.sql("""
					select
					A.name,
					A.ind_stage,
					A.operation,
					A.for_Quantity,
					A.transferred_qty,
					A.total_completed_qty,
					A.ind_rejection,
					IF(A.status="Completed", A.total_completed_qty-A.ind_rejection,0),
					A.total_time_in_mins,
					IF(A.docstatus="2","Cancelled",A.status),
					B.status

					FROM
					`tabJob Card` as A,
					`tabWork Order` as B

					WHERE
					A.work_order=B.name
					&& A.docstatus!="2"
					&& A.work_order = '%s'

					ORDER BY A.ind_stage ASC """ %(work_order), as_list=1)
