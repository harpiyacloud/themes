"""
    This model is used to create a product line fields like product template id,website id and label
"""

from harpiya import api, fields, models


class ProductLabelLine(models.Model):
    _name = "product.label.line"
    _description = 'Ürün Şablonu Etiket Satırı'

    product_tmpl_id = fields.Many2one('product.template', string='Ürün Şablonu ID', required=True)
    website_id = fields.Many2one('website', string="Web Site", required=True)
    label = fields.Many2one('product.label', required=True, string="Etiket", help="Ürün etiketinin adı")
    _sql_constraints = [('product_tmpl_id', 'unique (product_tmpl_id,website_id)',
                         'Etiket satırında yinelenen kayıtlara izin verilmiyor !')]
