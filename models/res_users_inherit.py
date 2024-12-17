from odoo import models, fields


class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one('employee.branch', string="Branch")
