from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Campos relacionados con la compañía para el banner de advertencia
    enable_warning_banner = fields.Boolean(
        string='Mostrar Banner de Advertencia',
        related='company_id.warning_banner_enabled',
        readonly=False,
        help="Activa esta opción para mostrar un banner de advertencia en la parte superior de todas las páginas del sistema."
    )

    warning_banner_text = fields.Text(
        string='Texto del Banner',
        related='company_id.warning_banner_text',
        readonly=False,
        help="Personaliza el mensaje que se mostrará en el banner de advertencia. Puedes usar texto largo y emojis."
    )

    @api.model
    def get_warning_banner_status(self):
        """
        Retorna el estado actual del banner de advertencia para la compañía actual.
        Útil para el frontend JavaScript.
        """
        company = self.env.company
        return {
            'enable_warning_banner': bool(company.warning_banner_enabled),
            'warning_text': company.warning_banner_text or '⚠️ FACTURA PENDIENTE DE PAGO',
        }