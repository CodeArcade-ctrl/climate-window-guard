"""Read climate/window states and expose whether ventilation is wasting energy."""

from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import UpdateFailed


async def async_read_sources(
    hass: HomeAssistant, window_entity: str, climate_entity: str
) -> dict[str, Any]:
    """Return the current window and HVAC action states."""
    window = hass.states.get(window_entity)
    climate = hass.states.get(climate_entity)
    if window is None or window.state in ("unknown", "unavailable"):
        raise UpdateFailed("The selected window sensor is unavailable")
    if climate is None or climate.state in ("unknown", "unavailable"):
        raise UpdateFailed("The selected climate entity is unavailable")

    window_open = window.state == "on"
    hvac_action = climate.attributes.get("hvac_action")
    alert = window_open and hvac_action in ("heating", "cooling")
    return {
        "window_open": window_open,
        "hvac_action": hvac_action or "idle",
        "alert": alert,
    }
