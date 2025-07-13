from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_warning_banner = fields.Boolean(
        string='Enable Warning Banner',
        config_parameter='custom_warning_banner.enable_warning_banner'
    )

    warning_banner_text = fields.Char(
        string='Banner Text',
        config_parameter='custom_warning_banner.warning_text',
        default='⚠️ FACTURA PENDIENTE DE PAGO'
    )

    @api.model
    def get_warning_banner_status(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        enable_param = ICPSudo.get_param('custom_warning_banner.enable_warning_banner', default='False')
        return {
            'enable_warning_banner': enable_param == 'True',
            'warning_text': ICPSudo.get_param(
                'custom_warning_banner.warning_text',
                default='⚠️ FACTURA PENDIENTE DE PAGO'
            )
        }