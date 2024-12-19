from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    source_id = fields.Many2one(
        'utm.source',
        string='Source',
        required=True,  # Enforce requirement at the ORM level
    )

    # Adding an ORM constraint to enforce it at the database level
    def _check_source_id(self):
        for record in self:
            if not record.source_id:
                raise ValidationError("The Source field is mandatory. Please select a value.")

    _constraints = [
        (_check_source_id, "The Source field is mandatory.", ['source_id']),
    ]