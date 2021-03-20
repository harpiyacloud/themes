"""
    This model is used to create a boolean social sharing options.
"""
import base64
from harpiya import fields, models, tools, api, _
from harpiya.modules.module import get_resource_path
from harpiya.addons.website.tools import get_video_embed_code


class res_config(models.TransientModel):
    _inherit = "res.config.settings"

    facebook_sharing = fields.Boolean(string='Facebook', related='website_id.facebook_sharing', readonly=False)
    twitter_sharing = fields.Boolean(string='Twitter', related='website_id.twitter_sharing', readonly=False)
    linkedin_sharing = fields.Boolean(string='Linkedin', related='website_id.linkedin_sharing', readonly=False)
    mail_sharing = fields.Boolean(string='E-posta', related='website_id.mail_sharing', readonly=False)
    is_load_more = fields.Boolean(string='Daha Fazla Yükle', related='website_id.is_load_more', readonly=False,
                                  help="Sonraki sayfa ürünlerini Ajax ile yükle")
    load_more_image = fields.Binary(string='Daha Fazla Yükle Görseli', related='website_id.load_more_image', readonly=False,
                                    help="Daha fazla yükleme uygulanırken bu resmi görüntüle.")
    button_or_scroll = fields.Selection([
        ('automatic', 'Otomatik- sayfa kaydırma'),
        ('button', 'Buton- tıklama butonu')
    ], string="Ürünler için yükleme türü", related='website_id.button_or_scroll',
        required=True, default='automatic', readonly=False,
        help="Mağaza sayfasında ürünlerin sayfa numaralandırmasının kaydırma veya düğme ile nasıl gösterileceğini "
             "tanımlayın.")
    prev_button_label = fields.Char(string='Önceki Buton Etiketi', related='website_id.prev_button_label',
                                    required=True, readonly=False, translate=True)
    next_button_label = fields.Char(string='Sonraki Butonun Etiketi', related='website_id.next_button_label',
                                    required=True, readonly=False, translate=True)
    is_lazy_load = fields.Boolean(string='Lazyload', related='website_id.is_lazy_load', readonly=False,
                                  help="Lazy load etkinleştirilecektir.")
    lazy_load_image = fields.Binary(string='Lazyload Resmi', related='website_id.lazy_load_image', readonly=False,
                                    help="Lazy Load yüklenirken bu görseli görüntüler.")
    banner_video_url = fields.Char(string='Video URL', related='website_id.banner_video_url',
                                   help='Banner için bir videonun URL\'si.', readonly=False)
    number_of_product_line = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ], string="Ürün adı için satır sayısı", related='website_id.number_of_product_line',
        required=True, default='1', readonly=False, help="Mağaza için ürün adında gösterilecek satır sayısı.")

    @api.onchange('is_load_more')
    def get_value_icon_load_more(self):
        if self.is_load_more == False:
            img_path = get_resource_path('theme_vega', 'static/src/img/Loadmore.gif')
            with tools.file_open(img_path, 'rb') as f:
                self.load_more_image = base64.b64encode(f.read())

    @api.onchange('is_lazy_load')
    def get_value_icon_lazy_load(self):
        if self.is_lazy_load == False:
            img_path = get_resource_path('theme_vega', 'static/src/img/Lazyload.gif')
            with tools.file_open(img_path, 'rb') as f:
                self.lazy_load_image = base64.b64encode(f.read())
