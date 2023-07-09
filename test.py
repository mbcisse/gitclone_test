# -*- coding: utf-8 -*-
{
    'name': "Carina Custom Addon",

    'summary': """
        Ceci est un Custom Addon implementé dans l'optique de pouvoir monter en compétences sur Odoo V16.
        Cet custom addon implemente la gestion d'une agence de location de Vehicules.""",

    'description': """
        Implementation d'un module de gestion de Location des voitures.
    """,

    'author': "Mohamed Bassirou CISSE",
    'website': "https://www.carina.consulting",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/agence_vehicule.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}
