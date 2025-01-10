{
    'name': 'Tijus Custom Base',
    'version': '17.0.1.0',
    'author': 'Tijus Academy',
    'summary': 'Handle custom settings',
    'depends': ['hr', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'data/project_task_data.xml',  # Add this line
        'views/employee_branch_view.xml',
        'views/hr_employee_inherit.xml',
        'views/branch_menu.xml',
        'views/project_task_views.xml',
    ],
    'license': 'LGPL-3',
    'application': False,
    'pre_init_hook': 'pre_init_hook',  # Changed from post_init_hook
}