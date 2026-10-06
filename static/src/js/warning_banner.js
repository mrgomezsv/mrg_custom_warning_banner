import { Component, onWillStart, proxy } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class WarningBanner extends Component {
    static template = "mrg_custom_warning_banner.WarningBanner";

    setup() {
        this.orm = useService("orm");
        // OWL 3 (Odoo 20): el estado reactivo se crea con proxy
        this.state = proxy({
            enabled: false,
            warningText: "⚠️ FACTURA PENDIENTE DE PAGO",
        });

        onWillStart(async () => {
            await this.loadBannerConfig();
        });
    }

    async loadBannerConfig() {
        try {
            const config = await this.orm.call(
                "res.company",
                "get_warning_banner_status",
                []
            );
            if (config) {
                this.state.enabled = Boolean(config.enable_warning_banner);
                this.state.warningText = config.warning_text || "⚠️ FACTURA PENDIENTE DE PAGO";
            }
        } catch (error) {
            console.error("Error loading warning banner config:", error);
            this.state.enabled = false;
        }
    }
}

// Registrar en el systray (barra superior)
export const systrayItem = {
    Component: WarningBanner,
};

registry.category("systray").add("warning_banner", systrayItem, { sequence: 1 });

