# -*- coding: utf-8 -*-

{
    'name': 'Adyen Payment Acquirer',
    'author': 'Odoo S.A',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Adyen Implementation',
    'version': '1.0',
    'description': """Adyen Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_adyen_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
}
