"""Binary sensors for Climate Window Guard."""

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

DESCRIPTION = BinarySensorEntityDescription(
    key="hvac_window_alert",
    translation_key="hvac_window_alert",
    device_class=BinarySensorDeviceClass.PROBLEM,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the alert sensor."""
    async_add_entities([ClimateWindowAlert(entry)])


class ClimateWindowAlert(CoordinatorEntity, BinarySensorEntity):
    """Turn on when a window is open during active heating or cooling."""

    entity_description = DESCRIPTION
    _attr_has_entity_name = True

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the alert entity."""
        super().__init__(entry.runtime_data)
        self._attr_unique_id = f"{entry.entry_id}_hvac_window_alert"

    @property
    def is_on(self) -> bool:
        """Return whether the window/HVAC combination should alert."""
        return self.coordinator.data["alert"]

    @property
    def extra_state_attributes(self) -> dict[str, str | bool]:
        """Explain the inputs behind the alert."""
        return {
            "window_open": self.coordinator.data["window_open"],
            "hvac_action": self.coordinator.data["hvac_action"],
        }
