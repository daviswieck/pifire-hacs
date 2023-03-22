import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "pifire"

DATA_SCHEMA = vol.Schema({vol.Required(CONF_IP_ADDRESS): cv.string})

class PifireFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Pifire."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Validate the IP address
            # TODO: Add IP address validation
            ip_address = user_input[CONF_IP_ADDRESS]

            return self.async_create_entry(title=ip_address, data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )
