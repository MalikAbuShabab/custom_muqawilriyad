from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    registration_number = fields.Char(string="Registration Number")
    capital = fields.Float(string="Capital")
    commercial_register_date = fields.Date(string="Commercial Register Date")
    url = fields.Char(string="URL")

    # Define the many2one relationship
    activity_type_ids = fields.Many2many(
        'company.activity',  # Model to which this field relates
        string="Activity Type"
    )









