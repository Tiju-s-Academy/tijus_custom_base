from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def _default_stage_id(self):
        return self.env['project.task.type'].search([], limit=1)

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'
    _order = 'sequence, id'

    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('blocked', 'Hold'),
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='new')
