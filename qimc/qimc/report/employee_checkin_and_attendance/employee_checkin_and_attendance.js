// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Checkin and Attendance"] = {
	"filters": [
	{
"fieldname":"from_date",
"label": __("From Date"),
"fieldtype": "Date",
"default": frappe.datetime.add_days(date,-7)
//"default": frappe.datetime.add_days(frappe.datetime.add_months(frappe.datetime.month_start(date),-1),14)
//"default": frappe.datetime.add_months(frappe.datetime.month_start(date),-1)
},

{
"fieldname":"to_date",
"label": __("To Date"),
"fieldtype": "Date",
"default": get_today()
},

{
"fieldname":"employee",
"label": __("Employee"),
"fieldtype": "Link",
"options": "Employee",
"default": "QIMC05"
},

{
"fieldname":"report_type",
"label": __("Report Type"),
"fieldtype": "Select",
"options":["Monthly Salary Summary","Daily Attendance Daitails"],
"default":"Daily Attendance Daitails"
}

	]
};
