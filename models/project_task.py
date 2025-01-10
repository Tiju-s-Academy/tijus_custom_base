from odoo import models, fields, api

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'
    _order = 'sequence, id'

    state = fields.Selection([
        ('01_in_progress', 'In Progress'),
        ('02_changes_requested', 'Changes Requested'),
        ('03_approved', 'Approved'),
        ('04_waiting_normal', 'Waiting'),
        ('05_hold', 'Hold'),
        ('06_pending', 'Pending'),
        ('1_done', 'Done'),
        ('1_canceled', 'Canceled')
    ], string='State', default='01_in_progress')
