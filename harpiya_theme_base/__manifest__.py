# noinspection PyStatementEffect
{
    # Theme information
    'name': 'Harpiya Tema Temeli',
    'category': 'Base',
    'summary': 'Tüm Harpiya e-Ticaret temaları için ortak kütüphaneler içeren temel modül.',
    'version': '2.0.6',
    'license': 'OPL-1',
    'depends': [
        'website_theme_install',
        'website_sale_wishlist',
        'website_sale_comparison',
        'website_blog',
    ],

    'data': [
        'templates/template.xml',
        'security/ir.model.access.csv',
        'views/social_sharing.xml',
    ],

    # Harpiya Store Specific
    'images': [
        'static/description/harpiya_theme_base.jpg',
    ],

    # Author
    'author': 'Harpiya Software Technologies',
    'website': 'https://www.harpiya.com',
    'maintainer': 'Harpiya Software Technologies',

    # Technical
    'installable': True,
    'auto_install': False,
}
