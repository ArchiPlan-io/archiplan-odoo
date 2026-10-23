{
    'name': 'ArchiPlan - Production Scheduling & Manufacturing Planning (APS)',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'ArchiPlan',
    'website': 'https://archiplan.io',
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Production scheduling, production planning and manufacturing scheduling for Odoo: an APS (advanced planning and scheduling) that turns your sales orders into a production schedule on people and machines, around shifts, skills and deadlines. Finite capacity scheduler, production planner, Gantt chart, job shop and shop floor scheduling, machine scheduling, workforce scheduling, shift scheduling, capacity planning, resource planning, make-to-order scheduling and reliable delivery dates. Set up by voice or text with an AI copilot.',
    'images': ['static/description/cover.png'],
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
