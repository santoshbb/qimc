from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Documents"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Workstation Type",
              "label": _("Workstation Type"),
              "description": _("Articles which members issue and return."),
            }
          ]
      },
      {
        "label":_("Reports"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "report",
              "is_query_report": True,
              "name": "Job Card Details",
              "doctype": "Job Card"
            },
            {
              "type": "report",
              "is_query_report": True,
              "name": "Project Task List",
              "doctype": "Task"
            },
            {
              "type": "report",
              "is_query_report": True,
              "name": "Quotation Analysis",
              "doctype": "Quotation"
            },
            {
              "type": "report",
              "is_query_report": True,
              "name": "Item Masters",
              "doctype": "Item"
            },

            {
              "type": "report",
              "is_query_report": True,
              "name": "Budget Statement",
              "doctype": "Budget"
            },
            {
                "type":"report",
                "is_query_report": True,
                "name": "Budget Variance With Percentage Report",
                "doctype": "Cost Center"
          }
        ]
      }
  ]
