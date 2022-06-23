# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters)
	data=get_data(filters)
	return columns, data

def get_columns(filters):
 #if filters.get("report_type"):
    if filters.get("report_type")=="Attendance Summary":
        return [
            _("Employee") + ":Link/Employee:90",
            _("Employee Name") + ":Data:150",
            _("Present") + ":Float:80",
            _("Absent") + ":Float:70",
            _("Leave") + ":Float:70",
            _("WFHome") + ":Float:90",
            _("WO") + ":Float:60",
            _("Total") + ":Float:120",
            _("Deductible Hours") + ":Float:140",
            _("Approved Hours") + ":Float:140"
        ]
        
    if filters.get("report_type")=="Attendance Details":
        return [
            _("Attendance ID") + ":Link/Attendance:130",
            _("Date") + ":Date:120",            
            _("Employee") + ":Link/Employee:90",
            _("Employee Name") + ":Data:150",
            _("Present") + ":Float:80",
            _("Absent") + ":Float:70",
            _("Leave") + ":Float:70",
            _("WFHome") + ":Float:90",
#            _("WO") + ":Float:60",
#            _("Total") + ":Float:120",
            _("Deductible Hours") + ":Float:140",
            _("Approved Hours") + ":Float:140"
        ]
        
    
def get_data(filters):
    from_date=filters.get("from_date")    
    to_date=filters.get("to_date")
    employee=filters.get("employee")
    if filters.get("report_type")=="Attendance Summary":
    #   from_date=filters.get("from_date")
    #   to_date=filters.get("to_date")
      return frappe.db.sql("""
		select
		A.employee,
		B.employee_name,
        sum(if(A.status="Present",1,0)),
        sum(if(A.status="Absent",1,0)),
        sum(if(A.status="On Leave",1,0)),
        sum(if(A.status="Work From Home",1,0)),
        (select count(name) from `tabHoliday` where parent = B.holiday_list and holiday_date >= '%s' and holiday_date <= '%s'),
        sum(if(A.status="Absent",1,0))+sum(if(A.status!="Absent",1,0))+(select count(name) from `tabHoliday` where parent = B.holiday_list and holiday_date >= '%s' and holiday_date <= '%s'),
        sum(A.ind_deductible_hours),
        sum(A.ind_approved_hours)

		FROM
		`tabAttendance` as A,
		`tabEmployee` as B
        
		WHERE
        A.employee=B.name
		&&A.attendance_date>='%s'
		&&A.attendance_date<='%s'
		&&A.docstatus="1"
		GROUP BY A.employee
		ORDER BY A.employee ASC 
        """ %(from_date,to_date,from_date,to_date, from_date,to_date), as_list=1)

    elif filters.get("report_type")=="Attendance Details":
    #  from_date=filters.get("from_date")
    #  to_date=filters.get("to_date")
      return frappe.db.sql("""
		select
		A.name,
        A.attendance_date,
        A.employee,
		B.employee_name,
        if(A.status="Present",1,0),
        if(A.status="Absent",1,0),
        if(A.status="On Leave",1,0),
        if(A.status="Work From Home",1,0),
#        (select count(name) from `tabHoliday` where parent = B.holiday_list and holiday_date >= '%s' and holiday_date <= '%s'),
#        if(A.status="Absent",1,0)+if(A.status!="Absent",1,0) + (select count(name) from `tabHoliday` where parent = B.holiday_list and holiday_date >= '%s' and holiday_date <= '%s'),
        A.ind_deductible_hours,
        A.ind_approved_hours
        
        FROM
        
		`tabAttendance` as A,
		`tabEmployee` as B
        
		WHERE
        A.employee=B.name
        && A.attendance_date>='%s'
        && A.attendance_date<='%s'
        && A.employee="%s"
        
        """ %(from_date,to_date, from_date,to_date,from_date,to_date,employee), as_list=1)