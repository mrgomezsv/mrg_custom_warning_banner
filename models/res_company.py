from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Campos para el banner de advertencia personalizable
    warning_banner_enabled = fields.Boolean(
        string='Habilitar Banner de Advertencia',
        default=False,
        help="Activa esta opción para mostrar un banner de advertencia en la parte superior de todas las páginas del sistema."
    )
    
    warning_banner_text = fields.Text(
        string='Texto del Banner de Advertencia',
        default='⚠️ FACTURA PENDIENTE DE PAGO',
        help="Personaliza el mensaje que se mostrará en el banner de advertencia. Puedes usar texto largo y emojis."
    )
