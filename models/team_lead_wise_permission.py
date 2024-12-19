from odoo import models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def _get_team_leader_domain(self):
        user = self.env.user
        if user.has_group('sales_team.group_sale_manager'):
            return []
        elif user.has_group('sales_team.group_sale_salesman_all_leads'):
            team_ids = self.env['crm.team'].search([('user_id', '=', user.id)]).ids
            return [('team_id', 'in', team_ids)]
        return [('id', '=', -1)]

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        domain = self._get_team_leader_domain()
        args = args + domain
        return super(CrmLead, self)._search(args, offset, limit, order, count, access_rights_uid)