# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "qimc"
app_title = "qimc"
app_publisher = "Akwad"
app_description = "ERP Customisations for QIMC"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "santosh.baburao@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qimc/css/qimc.css"
#app_include_css = "/qimc/public/css/custom.css"
#app_include_css = "/assets/qimc/css/custom.css"
# app_include_js = "/assets/qimc/js/qimc.js"

#000000000000000000000000 WEBVIEW 0000000000000000000000000
app_include_css = "/assets/qimc/css/akwad-desk.css"
web_include_css = "/assets/qimc/css/akwad-web.css"
web_include_js = "/assets/qimc/js/akwad-web.js"
#000000000000000000000000 WEBVIEW 000000000000000000000000

# include js, css files in header of web template
# web_include_css = "/assets/qimc/css/qimc.css"
# web_include_js = "/assets/qimc/js/qimc.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "qimc.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "qimc.install.before_install"
# after_install = "qimc.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qimc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {

#    "Leave Period": 
#    {
#        "validate": "qimc.hooks_call.leave_allocation.allocate_earned_leaves_to_employees_who_joined_last_month"
#    },
#        "Material Request": 
#    {
#        "validate": "qimc.hooks_call.material_request.sales_user_validation"
#    },

 	"Salary Structure Assignment": 
    {
        "onload": "qimc.hooks_call.salary_structure_assignment.calculate_gross_salary"
#        "on_update": "qimc.hooks_call.salary_structure_assignment.calculate_gross_salary"
    },

 	"Additional Salary": 
    {
        "validate": [

                    "qimc.hooks_call.additional_salary.validate_annual_leave_settlement",
                    "qimc.hooks_call.additional_salary.calculate_esb_settlement",
                    "qimc.hooks_call.additional_salary.calculate_overtime"

                    ]
    },

    "Salary Slip": 
    {
        "validate": "qimc.hooks_call.salary_slip.validate_calculate_end_date",
	"before_insert": "qimc.api.calculate_deductible_hours_salary_slip"
    },

#    "Stock Entry": {
#                "validate": "qimc.hooks_call.stock_entry.validate_purpose_manufacture"
#	},

 	"Loan": 
    {
 		"validate": "qimc.hooks_call.loan.duplicate_loan"
	},

	"Attendance": {
		"before_submit": "qimc.api.calculate_deductible_hours",
        "onload": "qimc.api.validate_approved_hours"
	}



#        "Leave Allocation": 
#   {
#       "validate": "qimc.hooks_call.leave_allocation.calculate_days_to_allocate"
#       "refresh": "qimc.hooks_call.leave_allocation.test"
#   },

}
#scheduler_events = {
#	"0 2 1 * *": [
#		"qimc.hooks_call.leave_allocation.allocate_earned_leaves_to_employees_who_joined_last_month"
#	]
#}
#doc_events = {
#	"Loan": {
#		"validate": "qimc.hooks_call.duplicate_loan"
#	}
#},
#------------------------------------------------------------------------------
#	"*": {
#		"validate": "footwear_erpnext.hooks_call.common.validate_all_doctype"
#	},
#	"Item": {
#		"autoname": "footwear_erpnext.hooks_call.item.autoname_custom_item",
#		"validate": ["footwear_erpnext.hooks_call.item.set_uom_and_warehouse",
#					"footwear_erpnext.hooks_call.item.validate_construction"]
#	},
#------------------------------------------------------------------------------
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qimc.tasks.all"
# 	],
# 	"daily": [
# 		"qimc.tasks.daily"
# 	],
# 	"hourly": [
# 		"qimc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qimc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"qimc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "qimc.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qimc.event.get_events"
# }
fixtures = [
            "Custom Field",
            "Client Script",
            "Print Format",
            "Report",
            "Workflow",
            "Workflow Action",
            "Letter Head"
            ]
