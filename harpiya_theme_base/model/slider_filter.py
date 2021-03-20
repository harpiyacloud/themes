"""
    This model is used to create a slider filter fields
"""
from harpiya import api, fields, models, _
from harpiya.tools.safe_eval import safe_eval
from harpiya.exceptions import UserError, ValidationError


class SliderFilter(models.Model):
    _name = "slider.filter"
    _order = "sequence asc"
    _description = "Slayt Filtresi"

    name = fields.Char(string="Adı", required=True, translate=True)
    sequence = fields.Integer(string='Sıra')
    website_published = fields.Boolean(string='Websitesinde Yayınla', default=True)
    filter_id = fields.Many2one('ir.filters', 'Filtre', required=True, help="Slayt ürünleri için ürün filtresi")
    slider_id = fields.Many2one('slider', string='Ürünü Filtrele')

    def website_publish_button(self):
        """
        Set slider filter published and unpublished on website
        :return:
        """
        if self.website_published:
            self.write({'website_published': False})
        else:
            self.write({'website_published': True})

    @api.onchange('filter_id')
    def _onchange_filter_id(self):
        """
        If selected Filter has no any product the raise the warning and remove that filter
        :return:
        """
        if self.filter_id:
            domain = safe_eval(self.filter_id.domain)
            domain += ['|', ('website_id', '=', None), ('website_id', '=', self.slider_id.website_id.id),
                       ('website_published', '=', True)]
            product_count = self.env['product.template'].sudo().search_count(domain)
            if product_count < 1:
                self.filter_id = False
                raise UserError(_('Üzgünüm! İçeriği sıfır olan filtre ayarlayamazsınız.'))
