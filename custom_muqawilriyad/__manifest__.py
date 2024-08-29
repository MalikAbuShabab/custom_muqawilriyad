{
    'name': 'Custom',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Custom',
    'summary': 'Module for managing partners and company activities',
    'depends': ['base','contacts'],
    'data': [
        'views/company_activity_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
