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

    _sql_constraints = [
        ('registration_number_unique', 'unique(registration_number)', 'The Activity Registration Number value must be unique!'),
    ]

    @api.constrains('registration_number')
    def _check_registration_number(self):
        for record in self:
            if self.search_count([('registration_number', '=', record.registration_number)]) > 1:
                raise ValidationError('The Activity Registration Number value must be unique!')









