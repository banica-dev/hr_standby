# -*- coding: utf-8 -*-
{
    'name': "hr_standby",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Daniel Banica",
    'website': "https://github.com/banica-dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_timesheet','hr_attendance','hr_holidays','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_standby_views.xml',
        'views/security.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'hr_standby/static/src/xml/**/*',
        ],
        'web.assets_backend': [
            'hr_standby/static/src/scss/hr_attendance.scss',
            'hr_standby/static/src/js/standby_attendance.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
