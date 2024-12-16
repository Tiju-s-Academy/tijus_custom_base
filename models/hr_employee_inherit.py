from odoo import models,fields


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    branch_id = fields.Many2one('employee.branch', string='Branch')
