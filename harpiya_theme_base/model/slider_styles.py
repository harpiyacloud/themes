"""
    This model is used to create a slider styles fields
"""
from harpiya import api, fields, models, _


class SliderStyles(models.Model):
    _name = "slider.styles"
    _description = "Slayt Stilleri"

    name = fields.Char(string='Adı', required=True)
    theme_id = fields.Many2one('ir.module.module', string="Şablon", required=True)
