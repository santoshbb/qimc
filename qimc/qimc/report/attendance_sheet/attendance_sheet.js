// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */
//from frappe.utils import today, getdate, get_last_day


frappe.query_reports["Attendance Sheet"] = {
//	onload: function() {
		//set current logged In Employee
//		if(frappe.session.user != "Administrator"){
//			frappe.db.get_value('Employee', {'user_id': frappe.session.user}, "name", function(value) {
//				frappe.query_report.set_filter_value('employee', value["name"]);
//			});
//		}
//		setTimeout(function(){  
//			if(frappe.query_report.get_filter_value('to_date') < frappe.datetime.add_days(frappe.datetime.month_start(date),14)){
//				var from_date = frappe.datetime.add_days(frappe.datetime.add_months(frappe.datetime.month_start(frappe.datetime.add_months(date, -1), -1),-1),14)
//				frappe.query_report.set_filter_value('from_date', from_date);
//			}
//			else{
//				var from_date = frappe.datetime.add_days(frappe.datetime.month_start(date),14)
//				frappe.query_report.set_filter_value('from_date', from_date);
//			}
//		}, 1000);
//	},
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(date,-10)
			//"default": frappe.datetime.add_days(frappe.datetime.month_start(date),14)
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname":"doc_status",
			"label": __("Attendance Status"),
			"fieldtype": "Read Only",
			"options": ["Draft","Submited","Cancelled"],
			"default": "Submited"
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
		},
		{
			"fieldname":"report_type",
			"label": __("Report Type"),
			"fieldtype": "Select",
			"options":["Attendance Summary","Attendance Details"],
			"default":"Attendance Summary"
		}
	]
};
