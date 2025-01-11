from odoo import fields, models

class HrEmployeePublicInherit(models.Model):
    _inherit = 'hr.employee.public'

    branch_id = fields.Many2one('employee.branch', string='Branch', related='employee_id.branch_id', readonly=False)
    agent_number = fields.Char('Voxbay Agent Number', related='employee_id.agent_number', readonly=False)
    related_joinee = fields.Many2one('employee.joining.form', string='Related Joinee', related='employee_id.related_joinee', readonly=False)
    biometric_no = fields.Char(string='Biometric Code', related='employee_id.biometric_no', readonly=False)
