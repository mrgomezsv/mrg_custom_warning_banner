from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    warning_banner_enabled = fields.Boolean(
        string='Enable Warning Banner',
        default=False,
    )
    warning_banner_text = fields.Char(
        string='Banner Text',
        default='⚠️ FACTURA PENDIENTE DE PAGO',
    )


