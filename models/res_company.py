from odoo import models, fields, api


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

    @api.model
    def get_warning_banner_status(self):
        """
        Retorna el estado del banner de advertencia para la compañía activa.
        Accesible para todos los usuarios autenticados.
        """
        company = self.env.company
        return {
            'enable_warning_banner': bool(company.warning_banner_enabled),
            'warning_text': company.warning_banner_text or '⚠️ FACTURA PENDIENTE DE PAGO',
            'company_id': company.id,
        }

