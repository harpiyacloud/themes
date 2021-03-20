{
    # Module information
    'name': 'Harpiya Product Tabs',
    'category': 'Website',
    'version': '1.0.0',
    'summary': 'This app contains to add new tabs in individual product',
    'license': 'OPL-1',

    # Dependencies
    'depends': [
        'harpiya_theme_base'
    ],

    # Views
    'data': [
        'views/product_tabs.xml',
        'security/ir.model.access.csv',
    ],
'images': [
	'static/description/harpiya_theme_product_tabs.jpg',
    ],
    # Author
    'author': 'Harpiya Software.',
    'website': 'http://www.harpiya.com',
   'maintainer': 'Harpiya Software.',

    # Technical
     'installable': True,
    'auto_install': False,
    'price': 0.00,
    'currency': 'EUR',
}
