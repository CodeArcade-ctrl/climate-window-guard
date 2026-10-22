"""Config flow for Climate Window Guard."""

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import selector

from .const import CONF_CLIMATE_ENTITY, CONF_WINDOW_ENTITY, DOMAIN


class ClimateWindowGuardConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Configure a window contact and climate entity."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Handle initial setup."""
        if user_input is not None:
            await self.async_set_unique_id(
                f"{user_input[CONF_WINDOW_ENTITY]}_{user_input[CONF_CLIMATE_ENTITY]}"
            )
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title="Climate Window Guard", data=user_input
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_WINDOW_ENTITY): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        filter=[{"domain": "binary_sensor", "device_class": "window"}]
                    )
                ),
                vol.Required(CONF_CLIMATE_ENTITY): selector.EntitySelector(
                    selector.EntitySelectorConfig(filter=[{"domain": "climate"}])
                ),
            }
        )
        return self.async_show_form(step_id="user", data_schema=schema)
