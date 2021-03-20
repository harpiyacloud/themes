"""
    This model is used to create a offer timer fields in pricelist
"""

from harpiya import fields, models


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    offer_msg = fields.Char(string="Teklif Mesajı", translate=True,
                            help="Mesajı ürün teklif zamanlayıcısında ayarlamak için.")
    is_display_timer = fields.Boolean(string='Zamanlayıcıyı Göster', help="Ürün sayfasında ürün zamanlayıcısını gösterir.")
