{
    'name': 'ArchiPlan Connector',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'ArchiPlan',
    'website': 'https://archiplan.io',
    'category': 'Manufacturing/Manufacturing',
    'depends': ['base_setup', 'mrp', 'sale'],
    'data': [
        'security/archiplan_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'views/res_config_settings_views.xml',
        'wizard/access_wizard_views.xml',
        'views/schedule_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'archiplan_connector/static/src/js/schedule.js',
            'archiplan_connector/static/src/xml/schedule.xml',
        ],
    },
    'installable': True,
    'application': False,
}
