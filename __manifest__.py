{
    'name': 'Coworking Management',
    'version': '17.0.1.0.0',
    'category': 'Services/Coworking',
    'summary': 'Manage rooms, desks, and bookings',
    'author': 'Emili',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [

        'data/ir_sequence_data.xml',
        'security/coworking_security.xml',
        'security/ir.model.access.csv',
        'wizard/quick_booking_wizard_view.xml',
        'views/coworking_views.xml',
        'views/coworking_menu.xml',
        'report/coworking_booking_report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
