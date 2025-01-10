from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Clean up task_status field from ir.model.fields
    cr.execute("""
        DELETE FROM ir_model_fields
        WHERE model = 'project.task' AND name = 'task_status';
    """)
    
    # Clean up mail tracking values
    cr.execute("""
        DELETE FROM mail_tracking_value
        WHERE field = 'task_status';
    """)

    # Clear the registry cache
    env.registry.clear_caches()
