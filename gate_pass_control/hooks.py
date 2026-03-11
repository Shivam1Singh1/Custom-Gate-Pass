app_name = "gate_pass_control"
app_title = "Gate Pass Control"
app_publisher = "Shivam Singh"
app_description = "Custom hide permission for Gate Pass"
app_email = "shivam.singh@microcrispr.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "gate_pass_control",
# 		"logo": "/assets/gate_pass_control/logo.png",
# 		"title": "Gate Pass Control",
# 		"route": "/gate_pass_control",
# 		"has_permission": "gate_pass_control.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gate_pass_control/css/gate_pass_control.css"

app_include_js = [
    "/assets/gate_pass_control/js/permission_manager_patch.js"
]

# include js, css files in header of web template
# web_include_css = "/assets/gate_pass_control/css/gate_pass_control.css"
# web_include_js = "/assets/gate_pass_control/js/gate_pass_control.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gate_pass_control/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page": "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype": "public/js/doctype.js"}
# doctype_list_js = {"doctype": "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype": "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype": "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "gate_pass_control/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# website_generators = ["Web Page"]

# Jinja
# ----------

# jinja = {
# 	"methods": "gate_pass_control.utils.jinja_methods",
# 	"filters": "gate_pass_control.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gate_pass_control.install.before_install"
# after_install = "gate_pass_control.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gate_pass_control.uninstall.before_uninstall"
# after_uninstall = "gate_pass_control.uninstall.after_uninstall"

# Integration Setup
# ------------------

# before_app_install = "gate_pass_control.utils.before_app_install"
# after_app_install = "gate_pass_control.utils.after_app_install"

# Integration Cleanup
# -------------------

# before_app_uninstall = "gate_pass_control.utils.before_app_uninstall"
# after_app_uninstall = "gate_pass_control.utils.after_app_uninstall"

# Desk Notifications
# ------------------

# notification_config = "gate_pass_control.notifications.get_notification_config"

# Permissions
# -----------

permission_query_conditions = {
    "Gate Pass": "gate_pass_control.overrides.gate_pass.get_permission_query_conditions"
}

has_permission = {
    "Gate Pass": "gate_pass_control.overrides.gate_pass.has_permission"
}

# DocType Class
# ---------------

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gate_pass_control.tasks.all"
# 	],
# 	"daily": [
# 		"gate_pass_control.tasks.daily"
# 	],
# 	"hourly": [
# 		"gate_pass_control.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gate_pass_control.tasks.weekly"
# 	],
# 	"monthly": [
# 		"gate_pass_control.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "gate_pass_control.install.before_tests"

# Overriding Methods
# ------------------------------

override_whitelisted_methods = {
    "frappe.core.page.permission_manager.permission_manager.update":
        "gate_pass_control.overrides.permission_manager.update",

    "attendee_life_cycle_custom.custom_scripts.gate_pass.share_doc_with_permission":
        "gate_pass_control.overrides.gate_pass.share_doc_with_permission",

    "attendee_life_cycle_custom.custom_scripts.gate_pass.set_employee_name_on_gate_pass":
        "gate_pass_control.overrides.gate_pass.set_employee_name_on_gate_pass",
}

# Fixtures
# ------------------------------

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["dt", "=", "DocPerm"], ["fieldname", "=", "hide"]]
    }
]

# override_doctype_dashboards = {
# 	"Task": "gate_pass_control.task.get_dashboard_data"
# }

# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------

# before_request = ["gate_pass_control.utils.before_request"]
# after_request = ["gate_pass_control.utils.after_request"]

# Job Events
# ----------

# before_job = ["gate_pass_control.utils.before_job"]
# after_job = ["gate_pass_control.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = []

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"gate_pass_control.auth.validate"
# ]

# export_python_type_annotations = True

# default_log_clearing_doctypes = {}

# Translation
# ------------

# ignore_translatable_strings_from = []