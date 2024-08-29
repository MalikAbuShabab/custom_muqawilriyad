from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CompanyActivity(models.Model):
    _name = 'company.activity'
    _description = 'Company Activity'


    name = fields.Char(string="Activity Name")
    activity_code = fields.Char(string="Activity Code")
    activity_description = fields.Char(string="Activity Description")

    _sql_constraints = [
        ('activity_code_unique', 'unique(activity_code)', 'The Activity Code value must be unique!'),
    ]

    @api.constrains('activity_code')
    def _check_activity_code(self):
        for record in self:
            if self.search_count([('activity_code', '=', record.activity_code)]) > 1:
                raise ValidationError('The Activity Code value must be unique!')



