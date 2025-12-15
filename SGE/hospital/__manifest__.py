# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Aplicacion gestion de un hospital",

    'description': """
Aplicacion gestion de un hospital
    """,

    'author': "Adrian Domingo",
    'website': "https://iesch.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/paciente.xml',
        'views/medico.xml',
        'views/ingreso.xml',
        'views/diagnostico.xml'
    ],
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

