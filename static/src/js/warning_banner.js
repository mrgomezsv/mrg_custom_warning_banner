/** @odoo-module **/

import { registry } from '@web/core/registry';
import { useService } from "@web/core/utils/hooks";
import { Component, onWillStart } from "@odoo/owl";

class WarningBanner extends Component {
    setup() {
        this.orm = useService("orm");
        this.enabled = false;

        onWillStart(async () => {
            const config = await this.orm.call(
                'res.config.settings',
                'get_warning_banner_status',
                []
            );
            this.enabled = config.enable_warning_banner || false;
        });
    }
}

WarningBanner.template = 'custom_warning_banner.WarningBanner';

const systrayRegistry = registry.category('systray');
systrayRegistry.add('warning_banner', {
    Component: WarningBanner,
    sequence: 100,
});