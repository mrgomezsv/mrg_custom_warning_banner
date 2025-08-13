from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_warning_banner = fields.Boolean(
        string='Enable Warning Banner',
        related='company_id.warning_banner_enabled',
        readonly=False,
    )

    warning_banner_text = fields.Char(
        string='Banner Text',
        related='company_id.warning_banner_text',
        readonly=False,
    )

    @api.model
    def get_warning_banner_status(self):
        company = self.env.company
        return {
            'enable_warning_banner': bool(company.warning_banner_enabled),
            'warning_text': company.warning_banner_text or '⚠️ FACTURA PENDIENTE DE PAGO',
        }