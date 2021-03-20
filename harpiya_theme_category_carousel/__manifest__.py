{
    #Module information
    'name': 'Harpiya Theme Category Slider',
    'category': 'eCommerce',
    'summary': 'This app contains part of category slider functionality for Harpiya eCommerce Themes.',
    'version': '1.0.0',
    'license': 'OPL-1',
    'depends':['harpiya_theme_base'],

    'data': [
	    'views/product_public_category.xml',
	    'templates/assets.xml'
    ],

    #Harpiya Store Specific
    'images': [
	'static/description/harpiya_theme_category_carousel.jpg',
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
