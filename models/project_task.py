from odoo import models, fields

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    state = fields.Selection(selection_add=[
        ('blocked', 'Hold'),  # Changed from 'hold' to 'blocked' to match XML
        ('pending', 'Pending')
    ])
