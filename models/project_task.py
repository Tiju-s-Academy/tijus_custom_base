from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    task_status = fields.Selection([
        ('normal', 'Normal'),
        ('hold', 'Hold'),
        ('pending', 'Pending')
    ], string='Task Status', default='normal', tracking=True)

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
