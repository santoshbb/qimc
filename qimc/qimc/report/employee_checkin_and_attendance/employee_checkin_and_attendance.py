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
    if filters.get("report_type")=="Daily Attendance Daitails":
        return [
            _("Employee Checkin") + ":Link/Employee Checkin:140",
            _("Employee Checkout") + ":Link/Employee Checkin:140",
            _("Attendance ID") + ":Link/Attendance:160",
            _("Attendance") + ":Data:100",
            _("Checkin") + ":Date:160",
            _("Checkout") + ":Date:160",
            _("Present Hours") + ":Float:120",
            _("Deductible Hours") + ":Float:130",
            _("Approved Hours") + ":Float:130"
        ]
    
    if filters.get("report_type")=="Monthly Salary Summary":
        return [
            _("Checkin") + ":Link/Employee Checkin:130",
            _("Checkout") + ":Link/Employee Checkin:130",
            _("WO") + ":float:150",
            _("Absent") + ":Float:100",
            _("Present") + ":Float:100",
            _("On Leave") + ":Float:100",
            _("Work From Home") + ":Float:140",
            _("Total Working Days-WO") + ":Float:180",
            _("Deductible Hours") + ":Float:140",
            _("Salary Slip") + ":Link/Salary Slip:180",
            _("Gross Paid") + ":Float:120",
            _("Total Deduction") + ":Float:120",
            _("Net Paid") + ":Float:120"
        ]
    
def get_data(filters):
    from_date=filters.get("from_date")    
    to_date=filters.get("to_date")
#    employee=filters.get("employee")    
    if filters.get("report_type")=="Daily Attendance Daitails":
        return frappe.db.sql("""
            select
#           if(A.log_type="IN",A.time,0),
            A.name,
            A.name,
            if(ISNULL(A.attendance),0,A.attendance),
            B.status,
            B.in_time,
            B.out_time,
            B.working_hours,
            if(B.status="Present",B.ind_deductible_hours,0),
            if(B.status="Present",B.ind_approved_hours,0)
					
            FROM
            `tabEmployee Checkin` as A,
            `tabAttendance` as B
        
            WHERE
            A.attendance=B.name
            && B.attendance_date>='%s'
            && B.attendance_date<='%s'

            GROUP BY B.attendance_date
            ORDER BY A.employee ASC, B.attendance_date DESC 
            """ %(from_date,to_date), as_list=1)

    elif filters.get("report_type")=="Monthly Salary Summary":
        from_date=filters.get("from_date")
        to_date=filters.get("to_date")
        from_date=filters.get("from_date")
        to_date=filters.get("to_date")
        from_date=filters.get("from_date")
        to_date=filters.get("to_date")
        return frappe.db.sql("""
        select
        A.employee,
        A.employee_name,
        B.holiday_list,
        sum(if(A.status="Absent",1,0)),
        sum(if(A.status="Present",1,0)),
        sum(if(A.status="On Leave",1,0)),
        sum(if(A.status="Work From Home",1,0)),
        sum(if(A.status="Absent",1,0))+sum(if(A.status!="Absent",1,0)),
        sum(A.ind_deductible_hours),
        C.name,
        C.gross_pay,
        C.total_deduction,
        C.net_pay
        
        FROM
        `tabAttendance` as A,
        `tabEmployee` as B,
        `tabSalary Slip` as C,
        `tabHoliday List` as D,
        `tabHoliday` as D1
        
        WHERE
        A.employee=B.name
        &&A.employee=C.employee
        &&B.holiday_list=D.name
        &&A.employee=B.name
        &&D.name=D1.parent
        &&A.attendance_date>='%s'
        &&A.attendance_date<='%s'
        &&C.posting_date>='%s'
        &&C.posting_date<='%s'
        &&D1.holiday_date>='%s'
        &&D1.holiday_date<='%s'
        &&A.docstatus="1"
        
        GROUP BY A.employee
        ORDER BY A.employee ASC 
        """ %(from_date,to_date,from_date,to_date,from_date,to_date), as_list=1)