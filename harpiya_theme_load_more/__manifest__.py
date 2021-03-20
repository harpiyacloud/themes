{
    #Module information
    'name': 'Harpiya Theme Load More',
    'category': 'eCommerce',
    'summary': 'This app provide the funcitonality of ajax scroll products in shop page.',
    'version': '1.0.0',
    'license': 'OPL-1',
    'depends':['harpiya_theme_base'],

    'data': [
        'views/load_more.xml',
	    'templates/assets.xml'
    ],

    #Harpiya Store Specific
    'images': [
		'static/description/harpiya_theme_load_more.jpg',
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
