"""The MYPV integration."""

import logging
from homeassistant.const import CONF_MONITORED_CONDITIONS
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import (
    ELECTRIC_CURRENT_AMPERE,
    FREQUENCY_HERTZ,
    TEMP_CELSIUS,
)

from .const import SENSOR_TYPES, DOMAIN, DATA_COORDINATOR
from .coordinator import MYPVDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Add an MYPV entry."""
    coordinator: MYPVDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        DATA_COORDINATOR
    ]

    entities = []

    if CONF_MONITORED_CONDITIONS in entry.options:
        for sensor in entry.options[CONF_MONITORED_CONDITIONS]:
            entities.append(MypvDevice(coordinator, sensor, entry.title))
    else:
        for sensor in entry.data[CONF_MONITORED_CONDITIONS]:
            entities.append(MypvDevice(coordinator, sensor, entry.title))
    async_add_entities(entities)


class MypvDevice(CoordinatorEntity):
    """Representation of a MYPV device."""

    def __init__(self, coordinator, sensor_type, name):
        """Initialize the sensor."""
        super().__init__(coordinator)
        if sensor_type not in SENSOR_TYPES:
            raise KeyError
        self._sensor = SENSOR_TYPES[sensor_type][0]
        self._name = name
        self.type = sensor_type
        self._data_source = SENSOR_TYPES[sensor_type][3]
        self.coordinator = coordinator
        self._last_value = None
        self._unit_of_measurement = SENSOR_TYPES[self.type][1]
        self._icon = SENSOR_TYPES[self.type][2]

        self.serial_number = self.coordinator.data["info"]["sn"]
        self.fwversion = self.coordinator.data["info"]["fwversion"]
        self.model = self.coordinator.data["info"]["device"]
        _LOGGER.debug(self.coordinator)

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name} {self._sensor}"

    @property
    def state(self):
        """Return the state of the device."""
        try:
            state = self.coordinator.data[self._data_source][self.type]
            if self.type == "power_act":
                rel_out = int(self.coordinator.data[self._data_source]["rel1_out"])
                load_nom = int(self.coordinator.data[self._data_source]["load_nom"])
                state = (rel_out * load_nom) + int(state)
            self._last_value = state
        except Exception as ex:
            _LOGGER.error(ex)
            state = self._last_value
        if state is None:
            return state
        if self._unit_of_measurement == FREQUENCY_HERTZ:
            return state / 1000
        if self._unit_of_measurement == TEMP_CELSIUS:
            return state / 10
        if self._unit_of_measurement == ELECTRIC_CURRENT_AMPERE:
            return state / 10
        return state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement this sensor expresses itself in."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return icon."""
        return self._icon

    @property
    def unique_id(self):
        """Return unique id based on device serial and variable."""
        return "{} {}".format(self.serial_number, self._sensor)

    @property
    def device_info(self):
        """Return information about the device."""
        return {
            "identifiers": {(DOMAIN, self.serial_number)},
            "name": self._name,
            "manufacturer": "MYPV",
            "model": self.model,
            "firmware": self.fwversion,
        }
