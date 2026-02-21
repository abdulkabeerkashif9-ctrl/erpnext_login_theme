import frappe
from frappe.website.page_renderers.template_page import TemplatePage

class LoginPageRenderer(TemplatePage):
    def can_render(self):
        return frappe.local.request.path in ("/login", "/login/")

    def render(self):
        frappe.local.response.update({
            "type": "redirect",
            "location": "/login"
        })
