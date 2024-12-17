{
    'name': 'Tijus Custom Base',
    'version': '17.0.1.0',
    'author': 'Tijus Academy',
    'summary': 'Handle custom settings',
    'depends': ['web','base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_inherit.xml',
        'views/employee_branch_view.xml',
        'views/res_users_inherit_view.xml',
        'views/branch_menu.xml',
    ],
    'license': 'LGPL-3',
    'application': False,
}