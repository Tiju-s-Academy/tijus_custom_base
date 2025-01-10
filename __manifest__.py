{
    'name': 'Tijus Custom Base',
    'version': '17.0.1.0',
    'author': 'Tijus Academy',
    'summary': 'Handle custom settings',
    'depends': ['hr', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_branch_view.xml',
        'views/hr_employee_inherit.xml',
        'views/branch_menu.xml',
        'views/project_task_views.xml',
    ],
    'license': 'LGPL-3',
    'application': False,
}