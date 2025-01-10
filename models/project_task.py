from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    task_status = fields.Selection([
        ('normal', 'Normal'),
        ('hold', 'Hold'),
        ('pending', 'Pending')
    ], string='Task Status', default='normal', tracking=True)

    state = fields.Selection([
        ('01_in_progress', 'In Progress'),
        ('02_changes_requested', 'Changes Requested'),
        ('03_approved', 'Approved'),
        ('04_waiting_normal', 'Waiting'),
        ('05_hold', 'Hold'),
        ('06_pending', 'Pending'),
        ('1_done', 'Done'),
        ('1_canceled', 'Canceled')
    ], string='State', default='01_in_progress', tracking=True)

    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self.stage_id:
            self.state = self.stage_id.state

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
