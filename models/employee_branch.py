from odoo import models, fields

class EmployeeBranch(models.Model):
    _name = 'employee.branch'
    _description = 'Employee Branch'

    name = fields.Char(string='Branch Name', required=True)
