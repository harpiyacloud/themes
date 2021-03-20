from harpiya import models


class ThemeFashion(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_fashion_post_copy(self, mod):
        self.disable_view('website_theme_install.customize_modal')
