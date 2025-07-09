from odoo import http
from odoo.http import request

class WarningBannerController(http.Controller):
    @http.route('/custom_warning_banner/check_banner', type='json', auth='user')
    def check_banner(self):
        param = request.env['ir.config_parameter'].sudo().get_param('custom_warning_banner.enable_warning_banner')
        return {'show_banner': param == 'True'}