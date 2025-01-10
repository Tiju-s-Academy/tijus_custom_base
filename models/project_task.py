from odoo import models, fields

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    state = fields.Selection(selection_add=[
        ('hold', 'Hold'),
        ('pending', 'Pending')
    ])
