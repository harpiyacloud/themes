{
    #Module information
    'name': 'Harpiya Theme Lazyload Image',
    'category': 'eCommerce',
    'summary': 'Shows images only when the visitor scrolls',
    'version': '1.0.0',
    'license': 'OPL-1',
    'depends':['harpiya_theme_base'],

    'data': [
        'views/lazy_load.xml',
        'templates/assets.xml'
    ],

    #Harpiya Store Specific
    'images': [
	'static/description/harpiya_theme_lazy_load.jpg',
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
