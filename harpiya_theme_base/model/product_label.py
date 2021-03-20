"""
    This model is used to create a product line field
"""
from harpiya import models, fields, api


class product_label(models.Model):
    _name = "product.label"
    _description = "Ürün Etiketi"

    name = fields.Char("Adı", required=True, translate=True, help="Satış etiketinin adı")
    font_html_color = fields.Char(
        string='Yazı Rengi',
        help="Burada, ürün etiketi metninin rengini görüntülemek için belirli bir HTML renk dizini (örn. # Ff0000) "
             "ayarlayabilirsiniz.")
    html_color = fields.Char(
        string='Renk',
        help="Burada, ürün etiketinin rengini görüntülemek için belirli bir HTML renk dizini (örn. # Ff0000) "
             "ayarlayabilirsiniz.")
    label_style = fields.Selection([
        ('style_1', 'Stil 1'),
        ('style_2', 'Stil 2'),
        ('style_3', 'Stil 3'),
        ('style_4', 'Stil 4'),
        ('style_5', 'Stil 5')
    ], string="Etiket stilini seçin",
        required=True, default='style_1', readonly=False)
