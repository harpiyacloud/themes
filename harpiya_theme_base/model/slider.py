"""
    This model is used to create a slider template
"""
from harpiya import api, fields, models, _
from harpiya.exceptions import UserError, ValidationError


class Slider(models.Model):
    _name = "slider"
    _inherit = ['website.published.multi.mixin']
    _description = "Carousel Slayt"

    name = fields.Char(string='Adı', required=True)
    website_id = fields.Many2one("website", string="Web Site", required=True)
    theme_id = fields.Many2one('ir.module.module', string="Tema", compute='_compute_theme')
    slider_filter_ids = fields.One2many("slider.filter", "slider_id", string="Filter",
                                        help="Slayt öğeleri için Ürün filtresini seçin")
    slider_style_id = fields.Many2one('slider.styles', string='Slayt Stili', required=True,
                                      help="Slayt stillerini seçin")
    slider_limit = fields.Integer(string='Slayt Limiti', default=10, required=True,
                                  help="Carousel Slayt limitini ayarlama")

    @api.depends('website_id')
    def _compute_theme(self):
        """
        Set a theme_id based in website
        :return:
        """
        self.theme_id = self.website_id.theme_id.id

    @api.onchange('website_id')
    def _onchange_website_id(self):
        """
        Remove a slider_style_id when website_id change
        :return:
        """
        self.slider_style_id = False

    def write(self, vals):
        """
        If it is product slider then slider_filter_ids is required else raise warning
        :param vals:
        :return:
        """
        res = super(Slider, self).write(vals)
        if not self.slider_filter_ids:
            raise UserError(_('Üzgünüm! Lütfen önce ürün filtrelerini ayarlayın'))
        else:
            return res

    @api.model
    def create(self, vals_list):
        """
        If it is product slider then slider_filter_ids is required else raise warning
        :param vals_list:
        :return:
        """
        res = super(Slider, self).create(vals_list)
        if not res.slider_filter_ids:
            raise UserError(_('Üzgünüm! Lütfen önce ürün filtrelerini ayarlayın'))
        else:
            return res

    def action_preview(self):
        """
        Redirecting to the preview controller
        :return:
        """
        url = '/slider-preview?rec_id=' + str(self.id)
        return {
            'name': ('Şablonu Düzenle'),
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }
