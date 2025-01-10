from odoo import api, SUPERUSER_ID

def pre_init_hook(cr):
    # Clean up task_status field completely
    cr.execute("SELECT id FROM ir_model_fields WHERE model = 'project.task' AND name = 'task_status'")
    field_ids = [r[0] for r in cr.fetchall()]
    
    if field_ids:
        # Remove tracking values
        cr.execute("DELETE FROM mail_tracking_value WHERE field IN %s", (tuple(field_ids),))
        # Remove field
        cr.execute("DELETE FROM ir_model_fields WHERE id IN %s", (tuple(field_ids),))
        # Remove mail tracking fields
        cr.execute("DELETE FROM mail_message WHERE tracking_value_ids @> %s", (tuple(field_ids),))
