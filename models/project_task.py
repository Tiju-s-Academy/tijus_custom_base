from odoo import models, fields, api

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

    @api.model
    def _get_state_selection(self):
        # Get original selection
        selections = self.env['project.task.type']._fields['state'].selection
        if not selections:
            selections = []
        # Add our new states
        return selections + [
            ('05_hold', 'Hold'),
            ('06_pending', 'Pending')
        ]

    state = fields.Selection(
        selection=_get_state_selection,
        string='State',
        default='01_in_progress'
    )
