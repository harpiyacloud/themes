from harpiya import api, fields, models, tools, _


class ProductTabLine(models.Model):
    _name = "product.tab.line"
    _description = 'Ürün Etiket Satırı'
    _order = "sequence, id"

    product_id = fields.Many2one('product.template', string='Ürün Şablonu')
    tab_name = fields.Char("Sekme Adı", required=True, translate=True)
    tab_content = fields.Html("Sekme İçeriği", sanitize_attributes=False, translate=True)
    website_ids = fields.Many2many('website', help="Açıklamayı belirli bir web sitesinde ayarlayabilirsiniz.")
    sequence = fields.Integer('Sekme Sırası', default=1, help="Sekme görüntüleme sırasını belirtebilirsiniz.")

    def checkTab(self, currentWebsite, tabWebsiteArray):
        if currentWebsite in tabWebsiteArray or len(tabWebsiteArray) == 0:
            return True
        else:
            return False
