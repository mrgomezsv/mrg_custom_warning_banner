{
    "name": "Custom Warning Banner",
    "version": "1.0",
    "summary": "Muestra un banner de advertencia en el backend, configurable por compañía (multi-compañía): activar/desactivar y definir texto personalizado por empresa desde Ajustes",
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