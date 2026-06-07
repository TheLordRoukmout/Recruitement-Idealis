{
    'name': 'Real Estate Sale',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'depends': ['sale_management', 'analytic', 'account', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/real_estate_project_views.xml',
        'views/sale_order_views.xml',
        'templates/website_project.xml',
        'report/sale_order_report.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'real_estate_sale/static/src/js/project_select.js',
        ],
    },
    'installable': True,
}