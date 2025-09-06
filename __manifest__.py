{
    "name": "⚠️ Banner de Advertencia Personalizado",
    "version": "1.0",
    "summary": "Muestra un banner de advertencia personalizable en el backend de Odoo",
    "description": """
        Banner de Advertencia Personalizado
        ===================================
        
        Este módulo permite mostrar un banner de advertencia personalizable en la parte superior 
        de todas las páginas del backend de Odoo.
        
        Características:
        * Configurable por compañía (multi-compañía)
        * Activar/desactivar el banner desde Ajustes
        * Texto personalizable por empresa
        * Interfaz intuitiva en Ajustes > Banner de Advertencia
        
        Configuración:
        1. Ve a Ajustes > Banner de Advertencia
        2. Activa "Mostrar Banner de Advertencia"
        3. Personaliza el texto del banner
        4. Guarda los cambios
    """,
    "depends": ["base", "web"],
    "data": [
        "views/res_config_settings_view.xml"
    ],
    'author': "Mario Roberto",
    'website': "https://mrgomezsv.github.io/",
    "assets": {
        "web.assets_backend": [
            "mrg_custom_warning_banner/static/src/xml/warning_banner.xml",
            "mrg_custom_warning_banner/static/src/js/warning_banner.js"
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}