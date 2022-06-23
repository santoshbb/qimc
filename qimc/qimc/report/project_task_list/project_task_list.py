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
		_("Task Name") + ":Data:330",
		_("Task ID") + ":Link/Task:150",
		_("Weight") + ":Float:80",
		_("Progress%") + ":Float:100",
		_("Overall%") + ":Float:100",
		_("Start Date") + ":Date:100",
		_("End Date") + ":Date:100",
		_("Status") + ":Data:100",
		_("Project") + ":Data:180"
	]

def get_data():
	return frappe.db.sql("""
	select
	A.subject,
	A.name,
	A.task_weight,
	A.progress,
	A.task_weight*A.progress/100,
	A.exp_start_date,
	A.exp_end_date,
	A.status,
	A.project

	FROM
	`tabTask` as A

    ORDER BY A.subject ASC
	""")