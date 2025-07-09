from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_warning_banner = fields.Boolean(string='Enable Warning Banner')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['enable_warning_banner'] = self.env['ir.config_parameter'].sudo().get_param('custom_warning_banner.enable_warning_banner', False)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('custom_warning_banner.enable_warning_banner', self.enable_warning_banner)

    @api.model
    def get_warning_banner_status(self):
        return {
            'enable_warning_banner': self.env['ir.config_parameter'].sudo().get_param('custom_warning_banner.enable_warning_banner', False)
        }