# noinspection PyStatementEffect
{
    'name': 'Vega Tema',
    'category': 'Theme/eCommerce',
    'summary': 'Tamamen Duyarlı, Temiz, Modern ve Kesitli Harpiya Teması. Mobilya, Moda, Elektronik, Güzellik, '
               'Sağlık ve Fitness, Mücevherat, Spor vb. Gibi e-Ticaret İşletmeler için uygundur.',
    'version': '1.4.2',
    'license': 'OPL-1',
    'depends': [
        'website_theme_install',
        'website_sale_wishlist',
        'sale_product_configurator',
        'harpiya_theme_product_carousel',
        'harpiya_theme_category_carousel',
        'harpiya_theme_quick_filter',
        'harpiya_theme_category_listing',
        'harpiya_theme_product_timer',
        'website_sale_stock',
        'harpiya_theme_load_more',
        'harpiya_theme_product_tabs',
        'harpiya_theme_product_label_extended',
        'harpiya_theme_landing_page',
        'harpiya_theme_lazy_load',
        'harpiya_theme_banner_video',
    ],

    'data': [
        'data/slider_styles_data.xml',
        'data/compare_data.xml',
        'templates/slider.xml',
        'templates/category.xml',
        'templates/compare.xml',
        'templates/assets.xml',
        'templates/harpiya_custom_snippets.xml',
        'templates/harpiya_default_snippets.xml',
        'templates/harpiya_default_buttons_style.xml',
        'templates/theme_customise_option.xml',
        'templates/customize.xml',
        'templates/blog.xml',
        'templates/shop.xml',
        'templates/login_popup.xml',
        'templates/header.xml',
        'templates/footer.xml',
        'templates/portal.xml',
        'templates/wishlist.xml',
        'templates/cart.xml',
        'templates/contactus.xml',
        'templates/quick_view.xml',
        'templates/price_filter.xml',
        'templates/product.xml',
        'templates/product_label.xml',
        'templates/ajax_cart.xml',
        'templates/menu_config.xml',
        'templates/404.xml',
        'templates/extra_pages.xml',
    ],

    # Harpiya Store Specific
    'images': [
        'static/description/main_poster.jpg',
        'static/description/main_screenshot.gif',
    ],

    # Author
    'author': 'Harpiya Software Technologies',
    'website': 'https://www.harpiya.com',
    'maintainer': 'Harpiya Software Technologies',

    # Technical
    'installable': True,
    'auto_install': False,
}
