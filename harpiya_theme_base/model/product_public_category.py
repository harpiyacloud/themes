"""
    This model is used to create a html field.
"""

from harpiya import api, fields, models, _
from harpiya.exceptions import UserError, ValidationError


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    allow_in_category_carousel = fields.Boolean(string='Kategori Carousel Slayt\'a İzin Ver',
                                                help="Bu kategoriyi carousel parçacıkları kategorisinde ayarlayabilirsiniz.")
    is_category_page = fields.Boolean(string='Kategori Sayfasına İzin Ver',
                                      help="Bu kategori için ayrı bir sayfa ayarlayacaktır")
    category_page = fields.Many2one("website.page", string="Select Page",
                                    help="Bu kategori için ayarlamak istediğiniz sayfayı seçin.")

    @api.constrains('allow_in_category_carousel')
    def validate_category_carousel(self):
        if not self.image_1920 and self.allow_in_category_carousel:
            raise ValidationError(
                _("Lütfen carousel'i ayarlamadan önce Kategori görüntüsünü ayarlayın"))
