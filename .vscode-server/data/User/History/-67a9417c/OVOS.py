# -*- coding: utf-8 -*-
{
    'name': "Tarea03ABM Hospital",

    'summary': "Tarea 03 --> Paciente y médicos",

    'description': """
Este módulo es la tarea03 de SGE 2023
    """,

    'author': "Adrian BM",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # Necesario para que se muestre:
    'application': True,
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # Aquí se le pasan las vistas
    'data': [
        'security/ir.model.access.csv',
        'views/vistaMedico.xml',
        'views/vistaPaciente.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

