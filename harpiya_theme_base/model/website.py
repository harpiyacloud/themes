import json

import werkzeug.urls
import werkzeug.utils
from harpiya.http import request
from harpiya.tools import image_process

import harpiya
from harpiya import fields, models, http
from harpiya.addons.auth_oauth.controllers.main import OAuthLogin
from harpiya.addons.website_sale_wishlist.controllers.main import WebsiteSaleWishlist


class Website(models.Model):
    _inherit = "website"

    def _get_default_header_content(self):
        return """
            <p></p>
            <div class="s_rating row te_s_header_offer_text">
            <ul>
                <li>İlk Siparişiniz için Özel Teklif</li>
                <li>
                    <section>|</section>
                </li>
                <li>Code : #ASDA44</li>
                <li>
                    <section>|</section>
                </li>
                <li>% 50 İndirim Kazanın</li>
            </ul>
            </div>
            """

    def _get_default_footer_extra_links(self):
        return """
        <section>
        <div class="te_footer_inline_menu">
            <ul class="te_footer_inline_menu_t">
                <li>
                    <section>
                        <a href="#">Hakkımızda</a>
                    </section>
                </li>
                <li>
                    <section>
                        <a href="#">İletişim</a>
                    </section>
                </li>
                <li>
                    <section>
                        <a href="#">Müşteri Hizmetleri</a>
                    </section>
                </li>
                <li>
                    <section>
                        <a href="#">Gizlilik Sözleşmesi</a>
                    </section>
                </li>
                <li>
                    <section>
                        <a href="#">Kullanım Şartları</a>
                    </section>
                </li>
                <li>
                    <section>
                        <a href="#">Mağazalarımız</a>
                    </section>
                </li>
            </ul>
        </section>
        </div>
        """

    def _get_default_footer_content(self):
        return """
            <p></p>
            <div class="row">
                <div class="col-lg-4 col-md-4 col-6">
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">Yardım</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Hediye Kartları</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Sipariş Durumu</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Ücretsiz Kargo</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Ürün Değişimi</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Uluslararası</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="col-lg-4 col-md-4 col-6">
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">Hakkımızda</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Kariyer</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Ortaklık</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Yapımcı ile Tanışın</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İletişim</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="col-lg-4 col-md-4 col-6">
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">Güvenlik</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Gizlilik</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Mesajlaşma</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Yasal</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Tedarik Zinciri</a>
                            </li>
                        </section>
                    </ul>
                </div>
            </div>
        """

    def _get_footer_style_3_content(self):
        return """
                <p></p>
                <section>
                    <div>
                        <h4 class="te_footer_menu_info">Bilgi</h4>
                    </div>
                </section>
                <div class="row">
                    <div class="col-lg-6 col-md-6 col-6">
                        <ul class="te_footer_info_ept">
                            <section>
                                <li>
                                    <a href="#">Yardım</a>
                                </li>
                            </section>


                            <section>
                                <li>
                                    <a href="#">Hediye Kartları</a>
                                </li>
                            </section>

                            <section>
                                <li>
                                    <a href="#">Sipariş Durumu</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">Ücretsiz Kargo</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">İade Değişim</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">Uluslararası</a>
                                </li>
                            </section>
                        </ul>
                    </div>
                    <div class="col-lg-6 col-md-6 col-6">
                        <ul class="te_footer_info_ept">

                            <section>
                                <li>
                                    <a href="#">Güvenlik</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">Gizlilik</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">Mesajlaşma</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">Yasal</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">Tedarik Zinciri</a>
                                </li>
                            </section>
                            <section>
                                <li>
                                    <a href="#">İletişim</a>
                                </li>
                            </section>
                        </ul>
                    </div>
                </div>"""
    def _get_footer_style_4_content(self):
        return """
         <p></p>
            <div class="row">
                <div class="footer-column-2 col-md-3 col-sm-6">
                    <div class="footer_top_title_div">
                        <h5 class="footer-sub-title">Mağazalarımız</h5>
                        <span>
                            <span class="fa fa-angle-down"></span>
                        </span>
                    </div>
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">İstanbul</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">London SF</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Cockfosters BP</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Los Angeles</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Chicago</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Las Vegas</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="footer-column-2 col-md-3 col-sm-6">
                    <div class="footer_top_title_div">
                        <h5 class="footer-sub-title">Bilgi</h5>
                        <span>
                            <span class="fa fa-angle-down"></span>
                        </span>
                    </div>
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">Mağazamız Hakkında</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Yeni Koleksiyon</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Kadın Elbisesi</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İletişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Son Haberler</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Site Haritası</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="footer-column-2 col-md-3 col-sm-6">
                    <div class="footer_top_title_div">
                        <h5 class="footer-sub-title">Bağlantılar</h5>
                        <span>
                            <span class="fa fa-angle-down"></span>
                        </span>
                    </div>
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">Gizlilik Politikası</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İade</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Kullanım Koşulları</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İletişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Son Haberler</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Site Haritası</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="footer-column-2 col-md-3 col-sm-6">
                    <div class="footer_top_title_div">
                        <h5 class="footer-sub-title">Altbilgi Menüsü</h5>
                        <span>
                            <span class="fa fa-angle-down"></span>
                        </span>
                    </div>
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <a href="#">Instagram Profili</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Yeni Koleksiyon</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Kadın Elbisesi</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İletişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Son Haberler</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Mağazalar</a>
                            </li>
                        </section>
                    </ul>
                </div>
            </div>
        """
    def _get_footer_style_5_content(self):
        return """
        <p></p>
            <div class="row">
                <div class="col-sm-6">
                    <div class="te_block_title">Hesabım</div>
                    <a class="te_collapse_icon collapsed" data-toggle="collapse" data-target="#my_account">
                        <div class="te_block_title_col">Hesabım</div>
                        <i class="fa fa-plus"></i>
                    </a>
                    <ul class="te_footer_info_ept collapse" id="my_account">
                        <section>
                            <li>
                                <a href="#">Hakkımızda</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İletişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Hesabım</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Sipariş Geçmişi</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Gelişmiş Arama</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="col-sm-6">
                    <div class="te_block_title">Yardım</div>
                    <a class="te_collapse_icon collapsed" data-toggle="collapse" data-target="#feature">
                        <div class="te_block_title_col">Özellikler</div>
                        <i class="fa fa-plus"></i>
                    </a>
                    <ul class="te_footer_info_ept collapse" id="feature">
                        <section>
                            <li>
                                <a href="#">Sıkça Sorulan Sorular</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">İade Değişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Müşteri Hizmetleri</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Promosyonlar</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="#">Mağazalarımız</a>
                            </li>
                        </section>
                    </ul>
                </div>
            </div>
        """
    def _get_footer_style_6_content(self):
        return """
        <p></p>
        <div class="row">
            <div class="col-sm-6 col-6 te_account_info">
                <div class="te_block_title">Hesabım</div>
                <ul class="te_footer_info_ept">
                    <section>
                        <li>
                            <a href="#">Yardım</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Hediye Kartları</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Sipariş Durumu</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Ücretsiz Kargo</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">İade Değişim</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Uluslararası</a>
                        </li>
                    </section>
                </ul>
            </div>
            <div class="col-sm-6 col-6">
                <div class="te_block_title">Kurumsal</div>
                <ul class="te_footer_info_ept">
                    <section>
                        <li>
                            <a href="#">Hakkımızda</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Kariyer</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Ortaklık</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">Promosyonlar</a>
                        </li>
                    </section>
                    <section>
                        <li>
                            <a href="#">İletişim</a>
                        </li>
                    </section>
                </ul>
            </div>
        </div>
        """

    def _get_footer_style_7_content(self):
        return """
            <p></p>
            <div class="row">
                <div class="col-md-6 col-6">
                    <div class="te_block_title">Bağlantılar</div>
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Yardım</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Hediye Kartları</a>
                            </li>
                        </section>
            
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Sipariş Durumu</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Ücretsiz Kargo</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">İade Değişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Uluslararası</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="col-md-6 col-6">
                    <div class="te_block_title">Harekete Geç</div>
                    <ul class="te_footer_info_ept">
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Güvenlik</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Gizlilik</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Mesajlaşma</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Yasal</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">Tedarik Zinciri</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <i class="fa fa-long-arrow-right"></i>
                                <a href="#">İletişim</a>
                            </li>
                        </section>
                    </ul>
                </div>
            </div>
        """
    def _get_default_header_extra_links(self):
        return """
            <p></p>
            <div class="te_header_static_menu">
                <ul>
                    <li>
                        <a href="#">Kuponlar</a>
                    </li>
                    <li>
                        <a href="#">Bilgi</a>
                    </li>
                    <li>
                        <a href="#">Hakkımızda</a>
                    </li>
                    <li>
                        <a href="#">Hakkımızda</a>
                    </li>
                </ul>
            </div>
        """
    def _get_default_vertical_menu(self):
        return """
            <section>
                <div class="te_sidenav_menu">
                    <ul>
                        <section>
                            <li>
                                <a href="/shop">Online Mağaza</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="/contactus">İletişim</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="/aboutus">Hakkımızda</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="/blog">Blog</a>
                            </li>
                        </section>
                        <section>
                            <li>
                                <a href="/shop">Koleksiyonlar</a>
                            </li>
                        </section>
                    </ul>
                </div>
                <div class="te_sidenav_content">
                    <section>
                        <p>Pellentesque mollis nec orci id tincidunt. Sed mollis risus eu nisi aliquet, sit amet
                            fermentum.
                        </p>
                    </section>
                </div>
            </section>
        """

    def _get_default_facebook(self):
        return """
            <span class="fa fa-facebook"/>
        """
    def _get_default_twitter(self):
        return """
            <span class="fa fa-twitter"/>
        """
    def _get_default_linkedin(self):
        return """    
            <span class="fa fa-linkedin"/>
        """
    def _get_default_youtube(self):
        return """    
            <span class="fa fa-youtube-play"/>
        """
    def _get_default_github(self):
        return """    
            <span class="fa fa-github"/>
        """
    def _get_default_instagram(self):
        return """    
            <span class="fa fa-instagram"/>
        """

    facebook_sharing = fields.Boolean(string='Facebook')
    twitter_sharing = fields.Boolean(string='Twitter')
    linkedin_sharing = fields.Boolean(string='Linkedin')
    mail_sharing = fields.Boolean(string='Mail')
    is_load_more = fields.Boolean(string='Daha Fazla', help="Daha fazla yükle etkinleştirilecek", readonly=False)
    load_more_image = fields.Binary('Daha Fazla Görseli', help="Daha fazla yükleme uygulanırken bu resmi görüntüle.",
                                    readonly=False)
    button_or_scroll = fields.Selection([
        ('automatic', 'Otomatik- sayfa kaydırma'),
        ('button', 'Buton- tıklama butonu')
    ], string="Ürünler için yükleme türü",
        required=True, default='automatic', readonly=False)
    prev_button_label = fields.Char(string='Önceki Buton Etiketi', required=True, readonly=False,
                                    default="Öncekini Yükle", translate=True)
    next_button_label = fields.Char(string='Sonraki Buton Etiketi', required=True, readonly=False,
                                    default="Sonrakini Yükle", translate=True)
    is_lazy_load = fields.Boolean(string='Lazyload', help="Lazy load etkinleştirilecek", readonly=False)
    lazy_load_image = fields.Binary('Lazyload Görseli', help="Lazy load yüklenirken bu görseli görüntüle.",
                                    readonly=False)
    banner_video_url = fields.Char(string='Video URL', help='Banner için bir videonun URL\'si.', readonly=False)
    number_of_product_line = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ], string="Ürün adı için satır sayısı", required=True, default='1', readonly=False, help="Mağaza için ürün adında gösterilecek satır sayısı.")
    website_company_info = fields.Text(string="Şirket Bilgisi", translate=True,
                                       default="We are a team of passionate people whose goal is to improve "
                                               "everyone's life through disruptive products. We build great products to solve your business problems.")
    website_footer_extra_links = fields.Html(string="Altbilgi İçeriği", translate=True,
                                             default=_get_default_footer_extra_links)
    website_header_offer_ept = fields.Html(string="Vefa Üstbilgi Teklif İçeriği", translate=True,sanitize=False,
                                           default=_get_default_header_content)
    footer_style_1_content_ept = fields.Html(string="Vega Altbilgi Stili 1 İçerik", translate=True,sanitize=False,
                                             default=_get_default_footer_content)
    footer_style_3_content_ept = fields.Html(string="Vega Altbilgi Stili 3 İçerik", translate=True,sanitize=False,
                                             default=_get_footer_style_3_content)
    footer_style_4_content_ept = fields.Html(string="Vega Altbilgi Stili 4 İçerik", translate=True,sanitize=False,
                                             default=_get_footer_style_4_content)
    footer_style_5_content_ept = fields.Html(string="Vega Altbilgi Stili 5 İçerik", translate=True,sanitize=False,
                                             default=_get_footer_style_5_content)
    footer_style_6_content_ept = fields.Html(string="Vega Altbilgi Stili 6 İçerik", translate=True, sanitize=False,
                                             default=_get_footer_style_6_content)
    footer_style_7_content_ept = fields.Html(string="Vega Altbilgi Stili 7 İçerik", translate=True, sanitize=False,
                                             default=_get_footer_style_7_content)
    website_header_extra_links = fields.Html(string="Vega Başlığı Ekstra İçeriği", translate=True, sanitize=False,
                                           default=_get_default_header_extra_links)
    website_vertical_menu_ept = fields.Html(string="Dikey Menü İçeriği", translate=True, sanitize=False,
                                           default=_get_default_vertical_menu)

    # @api.depends('banner_video_url')
    # def _compute_embed_code(self):
    #     for image in self:
    #         image.embed_code = get_video_embed_code(image.video_url)

    def getDatabase(self):
        """
                To display database in login popup
                :return: List of databases
                """
        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except harpiya.exceptions.AccessDenied:
            values['databases'] = None
        return values['databases']

    def category_check(self):
        """
        To display main parent product.public.category website specific
        :return:
        """
        return self.env['product.public.category'].sudo().search(
            [('parent_id', '=', False), ('website_id', 'in', (False, self.id))])

    def get_default_company_address(self):
        """
        To get company default address
        :return:
        """
        street = ''
        street2 = ''
        city = ''
        zip = ''
        state = ''
        country = ''

        getCurrentCompany = request.env['website'].get_current_website().company_id

        values = {
            'street': getCurrentCompany.street,
            'street2': getCurrentCompany.street2,
            'city': getCurrentCompany.city,
            'zip': getCurrentCompany.zip,
            'state_id': getCurrentCompany.state_id.name,
            'country_id': getCurrentCompany.country_id.name
        }

        if getCurrentCompany.street:
            street = str(values['street'])
        if getCurrentCompany.street2:
            street2 = str(values['street2'])
        if getCurrentCompany.city:
            city = str(values['city'])
        if getCurrentCompany.zip:
            zip = values['zip']
        if getCurrentCompany.state_id.name:
            state = str(values['state_id'])
        if getCurrentCompany.country_id.name:
            country = str(values['country_id'])

        return street +' '+ street2 +' '+ city + ' '+ zip + ' '+ state + ' '+ country

    def get_product_categs_path(self, id):
        """
        To render full path for breadcrumbs based on argument
        :param id: product.public.category
        :return: list of category path and website url
        """
        categ_set = []
        if id:
            while id:
                categ = self.env['product.public.category'].sudo().search([('id', '=', id)])
                categ_set.append(categ.id)
                if categ and categ.parent_id:
                    id = categ.parent_id.id
                else:
                    break

        # For Reverse order
        categ_set = categ_set[::-1]

        values = {
            'categ_set': categ_set,
            'web_url': self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        }
        return values

    def get_min_max_prices(self, search=False, category=False, attributes=False):
        """
        Get minimum price and maximum price according to Price list as well as discount for Shop page
        :return: min and max price value
        """
        range_list = []
        cust_min_val = request.httprequest.values.get('min_price', False)
        cust_max_val = request.httprequest.values.get('max_price', False)

        domain = WebsiteSaleWishlist._get_search_domain(self, search=search, category=category,
                                                        attrib_values=attributes)

        if attributes:
            ids = []
            for value in attributes:
                if value[0] == 0:
                    ids.append(value[1])
                    domain += [('product_brand_ept_id.id', 'in', ids)]
        products = self.env['product.template'].search(domain)
        prices_list = []
        if products:
            pricelist = self.get_current_pricelist()
            for prod in products:
                context = dict(self.env.context, quantity=1, pricelist=pricelist.id if pricelist else False)
                product_template = prod.with_context(context)

                list_price = product_template.price_compute('list_price')[product_template.id]
                price = product_template.price if pricelist else list_price
                if price:
                    prices_list.append(price)

        if not prices_list: return False

        if not cust_min_val and not cust_max_val:
            range_list.append(min(prices_list))
            range_list.append(max(prices_list))
            range_list.append(round(min(prices_list),2))
            range_list.append(round(max(prices_list),2))
        else:
            range_list.append(cust_min_val)
            range_list.append(cust_max_val)
            range_list.append(round(min(prices_list), 2))
            range_list.append(round(max(prices_list), 2))
        return range_list

    def get_brand(self, products=False):
        """
        This function is used to search the list of brand data
        :return: List of brand
        """

        if products:
            shop_brands = self.env['product.brand.ept'].sudo().search([('product_ids', 'in', products.ids), ('products_count', '>', 0),('website_id', 'in', (False, self.get_current_website().id))])
        else:
            shop_brands = self.env['product.brand.ept'].sudo().search(
                [('website_published', '=', True), ('products_count', '>', 0),
                 ('website_id', 'in', (False, self.get_current_website().id))])
        return shop_brands

    def image_resize(self, img, width, height):
        """
        This function is used for resize the image with specific height and width
        and return the resizable image.
        :param img: image url
        :param width: image width
        :param height: image height
        :return: resizable image url
        """
        return image_process(img, size=(width, height))

    def get_carousel_category_list(self):
        """
        This method is used for return the list of category
        which has selected the allow category in carousel option from admin
        :return: list of category.
        """
        domain = [('website_id', 'in', (False, self.get_current_website().id)),
                  ('allow_in_category_carousel', '=', True)]
        category = self.env['product.public.category'].sudo().search(domain)
        return category

    def checkQuickFilter(self, currentWebsite, filterWebsiteArray):
        if currentWebsite in filterWebsiteArray or len(filterWebsiteArray) == 0:
            return True
        else:
            return False

    def list_providers_ept(self):
        """
        This method is used for return the encoded url for the auth providers
        :return: link for the auth providers.
        """
        try:
            providers = request.env['auth.oauth.provider'].sudo().search_read([('enabled', '=', True)])
        except Exception:
            providers = []
        for provider in providers:
            return_url = request.httprequest.url_root + 'auth_oauth/signin'
            state = OAuthLogin.get_state(self, provider)
            params = dict(
                response_type='token',
                client_id=provider['client_id'],
                redirect_uri=return_url,
                scope=provider['scope'],
                state=json.dumps(state),
            )
        return werkzeug.url_encode(params)
