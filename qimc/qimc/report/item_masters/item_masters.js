// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Masters"] = {
    "filters":[

    {
    "fieldname":"details",
    "label" :("Details"),
    "fieldtype":"Select",
    "options":["Less Details","More Details"],
    "default":"More Details"
    },

    {
    "fieldname":"item_group",
    "label":("Item Group"),
    "fieldtype":"Link",
    "options":"Item Group"
    }
]
}