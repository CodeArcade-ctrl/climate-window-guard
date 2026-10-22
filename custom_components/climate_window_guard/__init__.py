"""Climate Window Guard integration."""

from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import CONF_CLIMATE_ENTITY, CONF_WINDOW_ENTITY, DOMAIN
from .coordinator import async_read_sources

PLATFORMS: list[Platform] = [Platform.BINARY_SENSOR]
_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the configured window/climate pair."""
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_method=lambda: async_read_sources(
            hass,
            entry.data[CONF_WINDOW_ENTITY],
            entry.data[CONF_CLIMATE_ENTITY],
        ),
        update_interval=timedelta(seconds=15),
    )
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload the integration platforms."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
