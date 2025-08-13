# pyright: reportMissingImports=false
from odoo import http  # type: ignore
from odoo.http import request  # type: ignore


class WarningBannerController(http.Controller):
    @http.route('/custom_warning_banner/check_banner', type='json', auth='user')
    def check_banner(self):
        company = request.env.company
        return {
            'show_banner': bool(company.warning_banner_enabled),
            'warning_text': company.warning_banner_text or '⚠️ FACTURA PENDIENTE DE PAGO',
        }