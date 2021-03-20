{
    #Module information
    'name': 'Harpiya Theme Quick Filter',
    'category': 'eCommerce',
    'summary': 'This app contains the part of quick filter functionality for Harpiya eCommerce Themes.',
    'version': '1.0.0',
    'license': 'OPL-1',
    'depends':['harpiya_theme_base'],

    'data': [
        'views/quick_filter_view.xml',
        'templates/assets.xml'
    ],

    #Harpiya Store Specific
    'images': [
	'static/description/harpiya_theme_quick_filter.jpg',
    ],

    # Author
    'author': 'Harpiya Software.',
    'website': 'https://www.harpiya.com',
    'maintainer': 'Harpiya Software.',

    # Technical
    'installable': True,
    'auto_install': False,
    'price': 0.00,
    'currency': 'EUR',
}
