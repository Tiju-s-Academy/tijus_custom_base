from odoo import fields,models


class HrEmployeePublicInherit(models.Model):
    _inherit = 'hr.employee.public'

    branch_id = fields.Many2one('employee.branch', string='Branch')
    agent_number = fields.Char('Voxbay Agent Number')
    related_joinee = fields.Many2one('employee.joining.form',string='Related Joinee')

