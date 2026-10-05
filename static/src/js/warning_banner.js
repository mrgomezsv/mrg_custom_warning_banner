import { Component, onWillStart, proxy } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class WarningBanner extends Component {
    static template = "mrg_custom_warning_banner.WarningBanner";

    setup() {
        this.orm = useService("orm");
        this.companyService = useService("company");
        // OWL 3 (Odoo 20) ya no tiene useState: el estado reactivo se crea con proxy
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
            // Pasar el contexto con allowed_company_ids para asegurar multi-compañía
            const config = await this.orm.call(
                "res.config.settings",
                "get_warning_banner_status",
                [],
                { context: { allowed_company_ids: this.companyService.allowedCompanyIds } }
            );
            this.state.enabled = config.enable_warning_banner || false;
            this.state.warningText = config.warning_text || "⚠️ FACTURA PENDIENTE DE PAGO";
        } catch (error) {
            console.error("Error loading warning banner config:", error);
            this.state.enabled = false;
        }
    }
}

// Registrar en el systray (barra superior)
registry.category("systray").add("warning_banner", { Component: WarningBanner }, { sequence: 1 });
