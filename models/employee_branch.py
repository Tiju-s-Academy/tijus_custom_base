from odoo import models,fields


class EmployeeBranch(models.Model):
    _name = 'employee.branch'

    name = fields.Char(string='Branch', required=True)