{
    'name': 'Parking Management',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'license': 'LGPL-3',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/parking_client_views.xml',
        'views/parking_place_views.xml',
        'templates/parking_website.xml',
    ],
    'installable': True,
}