"""
    This model is used to show the tab line filed in product template
"""
from harpiya.exceptions import Warning
from harpiya import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    label_line_ids = fields.One2many('product.label.line', 'product_tmpl_id', 'Ürün Etiketleri',
                                     help="Ürün etiketi sayısını ayarlama")
    product_brand_ept_id = fields.Many2one(
        'product.brand.ept',
        string='Marka',
        help='Bu ürün için bir marka seçin'
    )
    tab_line_ids = fields.One2many('product.tab.line', 'product_id', 'Ürün Sekmeleri', help="Ürün sekmelerini ayarlama")

    @api.constrains('tab_line_ids')
    def check_tab_lines(self):
        if len(self.tab_line_ids) > 4:
            raise Warning("4'ten fazla sekme oluşturamazsınız!!")
