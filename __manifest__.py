{
    'name': 'Tijus Custom Base',
    'version': '17.0.1.0',
    'author': 'Tijus Academy',
    'summary': 'Handle custom settings',
    'depends': ['hr', 'project', 'new_python_model'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_branch_view.xml',
        'views/hr_employee_inherit.xml',
        'views/branch_menu.xml',
        'data/project_task_data.xml',
    ],
    'license': 'LGPL-3',
    'application': False,
}