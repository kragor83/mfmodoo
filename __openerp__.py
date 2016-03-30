# -*- coding: utf-8 -*-
{
    'name': "My First Module(База Сотрудников)",
    'description': """
    База сотрудников написанная в качестве тестового задания
    """,

    'author': "Maksim Krasnov",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'sequence': 0,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
}
