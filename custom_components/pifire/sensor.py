import logging

import aiohttp
import async_timeout
import json

from homeassistant.const import (
    CONF_IP_ADDRESS,
    CONF_NAME,
    TEMP_FAHRENHEIT,
)
from homeassistant.helpers.entity import Entity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "current_temperature": ["Current Temperature", "°F", "mdi:thermometer"],
    "current_setpoints": ["Current Setpoints", "°F", "mdi:thermometer-lines"],
    "current_status": ["Current Status", None, "mdi:information-outline"],
    "control": ["Control", None, "mdi:information-outline"],
    "settings": ["Settings", None, "mdi:information-outline"],
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add sensors for a new Pifire integration."""
    ip_address = config_entry.data[CONF_IP_ADDRESS]
    name = config_entry.data[CONF_NAME]

    async_add_entities(
        [
            PifireSensor(ip_address, name, sensor_type)
            for sensor_type in SENSOR_TYPES
        ]
    )

class PifireSensor(Entity):
    """Define a Pifire sensor."""

    def __init__(self, ip_address, name, sensor_type):
        """Initialize the sensor."""
        self._ip_address
