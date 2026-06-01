# -*- coding: utf-8 -*-
{
    'name': "videoclub",

    'summary': "Aplicación para la gestión de un videoclub",

    'description': """
Permite gestionar un videoclub con peliculas, categorias, clientes, alquileres y actores
    """,

    'author': "Adrián Domingo",
    'website': "https://iesch.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/pelicula.xml',
        'views/actor.xml',
        'views/categoria.xml',
        'views/cliente.xml',
        'views/alquiler.xml',
        'views/incidencia.xml',
        'views/reports.xml',
        'views/alquiler_wyzard.xml',
    ],
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

