from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    source_id = fields.Many2one(
        'utm.source',  # Related model
        string='Source',  # Field label
        required=True,  # Make the field mandatory
        ondelete='set null',  # Behavior when the related record is deleted
        help="This field indicates the source of the lead."  # Tooltip/help text
    )
