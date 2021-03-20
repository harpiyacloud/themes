{
    #Module information
    'name': 'Harpiya Theme Brand',
    'category': 'eCommerce',
    'summary': 'This app contains part of brand functionality for Harpiya eCommerce Themes.',
    'version': '1.1.0',
    'license': 'OPL-1',
    'depends':['harpiya_theme_base'],

    'data': [
        'views/product_template.xml',
        'views/product_brand_ept.xml',
        'templates/assets.xml',
	    'security/ir.model.access.csv',
    ],

    #Harpiya Store Specific
    'images': [
	'static/description/harpiya_theme_brand.jpg',
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
