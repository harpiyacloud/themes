{
    'name': 'Agora Tema',
    'category': 'Theme/eCommerce',
    'summary': 'Tamamen Duyarlı, Temiz, Modern ve Kesitli Harpiya Teması. Mobilya, Moda, Elektronik, Güzellik, '
               'Sağlık ve Fitness, Mücevherat, Spor vb. Gibi e-Ticaret İşletmeler için uygundur.',
    'sequence': 100,
    'version': '1.0',
    'depends': [
        'website_theme_install',
        'website_sale_wishlist',
        'sale_product_configurator',
        'website_sale_stock',
    ],
    'data': [
        'views/assets.xml',
        'templates/headers.xml',
        'templates/footer.xml',
    ],
    'images': [
        'static/description/bootswatch.png',
        'static/description/bootswatch_screenshot.jpg',
    ],
    'author': 'Harpiya Software Technologies',
    'website': 'https://www.harpiya.com',
    'maintainer': 'Harpiya Software Technologies',

    'application': False,
}
