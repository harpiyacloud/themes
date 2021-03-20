"""
    This model is used to create a quick filter boolean field in attributes
"""

from harpiya import fields, models


class ProductAttribute(models.Model):
    _inherit = ['product.attribute']

    is_quick_filter = fields.Boolean(string='Hızlı Fitre', help="Bu özellik hızlı filtrede gösterilecek")
    website_ids = fields.Many2many('website', help="Filtreyi belirli bir web sitesinde ayarlayabilirsiniz.")
