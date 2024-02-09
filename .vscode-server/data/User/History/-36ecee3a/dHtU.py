# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",

    'summary': "Lista de tareas Tarea01 ABM",

    'description': """
                    Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo
                    modelo de datos
                    """,

    'author': "Adrián Ballester",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application' : True,
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ]
    
}

