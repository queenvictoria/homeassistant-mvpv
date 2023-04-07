"""Constants for the MYPV piko integration."""
from datetime import timedelta
from dataclasses import dataclass

from homeassistant.const import (
    UnitOfPower,
    UnitOfElectricPotential,
    UnitOfElectricCurrent,
    UnitOfFrequency,
    UnitOfTemperature,
    UnitOfTime,
    PERCENTAGE,
    Platform,
)

DOMAIN = "mypv"

PLATFORMS = [Platform.SENSOR]

DATA_COORDINATOR = "coordinator"

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=10)

# short name . long name
MYPV_DEVICES = {
    "AC ELWA-E": "elwa",
    "AC-THOR": "acthor",
    "AC-THOR 9s": "actor9s",
    "AC ELWA-2": "elwa2",
    "Wi-Fi Meter": "meter",
}


@dataclass
class S:
    name_long: str
    unit: str = None
    icon: str = ""
    device: str = ""
    source: str = "data"


# sensor_type: [name, unit, icon, page, devices]
SENSOR_TYPES = {
    "device": S("Device"),
    "acthor9s": S("Acthor 9s"),
    "fwversion": S("Firmware Version", icon="mdi:numeric"),
    "psversion": S("Power Supply Version", icon="mdi:numeric"),
    "p9sversion": S("Power Supply Version Acthor 9", icon="mdi:numeric"),
    "screen_mode_flag": S("Screen Mode"),
    "status": S("Status ID", device="elwa acthor acthor9s elwa2"),
    "power": S(
        "Aktueller Verbrauch", UnitOfPower.WATT, "mdi:lightning-bolt", device="elwa"
    ),
    "boostpower": S(
        "Warmwassersicherstellung",
        UnitOfPower.WATT,
        "mdi:thermometer-lines",
        device="elwa",
    ),
    "power_act": S(
        "Power AC-Thor", UnitOfPower.WATT, "mdi:lightning-bolt", device="acthor"
    ),
    "power_solar_act": S(
        "Power from solar", UnitOfPower.WATT, "mdi:solar-power-variant"
    ),
    "power_grid_act": S(
        "Power from grid", UnitOfPower.WATT, "mdi:transmission-tower-export"
    ),
    "power_ac9": S("Power Acthor 9", UnitOfPower.WATT, "mdi:lightning-bolt"),
    "power_solar_ac9": S(
        "Power from solar Acthor 9", UnitOfPower.WATT, "mdi:solar-power-variant"
    ),
    "power_grid_ac9": S(
        "Power from grid Acthor 9", UnitOfPower.WATT, "mdi:transmission-tower-export"
    ),
    "power1_solar": S("power1_solar", UnitOfPower.WATT, "mdi:solar-power-variant"),
    "power1_grid": S("power1_grid", UnitOfPower.WATT, "mdi:transmission-tower-export"),
    "power2_solar": S("power2_solar", UnitOfPower.WATT, "mdi:solar-power-variant"),
    "power2_grid": S("power2_grid", UnitOfPower.WATT, "mdi:transmission-tower-export"),
    "power3_solar": S("power3_solar", UnitOfPower.WATT, "mdi:solar-power-variant"),
    "power3_grid": S("power3_grid", UnitOfPower.WATT, "mdi:transmission-tower-export"),
    "load_state": S("load_state"),
    "load_nom": S("load_nom", UnitOfPower.WATT),
    "rel1_out": S("rel1_out", icon="mdi:electric-switch"),
    "ww1target": S(
        "target_temperature",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer-auto",
        device="elwa",
    ),
    "temp1": S(
        "Speicher Temperatur 1",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer-water",
        device="elwa acthor acthor9s elwa2",
    ),
    "temp2": S(
        "Temperatur 2",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        device="acthor acthor9s",
    ),
    "temp3": S(
        "Temperatur 3",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        device="acthor acthor9s",
    ),
    "temp4": S(
        "Temperatur 4",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        device="acthor acthor9s",
    ),
    "boostactive": S("Boost active", icon="mdi:thermometer-chevron-up"),
    "legboostnext": S("Nächster Legionellen Boost", UnitOfTime.DAYS, "mdi:bacteria"),
    "date": S("Date", icon="mdi:calendar-today"),
    "loctime": S("Lokale Uhrzeit", icon="mdi:home-clock"),
    "unixtime": S("Unix time", icon="mdi:web-clock"),
    "wp_flag": S("wp_flag"),
    "wp_time1_ctr": S("wp_time1_ctr"),
    "wp_time2_ctr": S("wp_time2_ctr"),
    "wp_time3_ctr": S("wp_time3_ctr"),
    "pump_pwm": S("Pump PWM", icon="mdi:pump"),
    "schicht_flag": S("Schicht"),
    "act_night_flag": S("Night flag"),
    "ctrlstate": S("ctrlstate"),
    "blockactive": S("Block active"),
    "error_state": S("Error state", icon="mdi:alert-circle"),
    "meter1_id": S("my-PV Meter 1 ID", icon="mdi:identifier"),
    "meter1_ip": S("my-PV Meter 1 IP", icon="mdi:ip-network"),
    "meter2_id": S("my-PV Meter 2 ID", icon="mdi:identifier"),
    "meter2_ip": S("my-PV Meter 2 IP", icon="mdi:ip-network"),
    "meter3_id": S("my-PV Meter 3 ID", icon="mdi:identifier"),
    "meter3_ip": S("my-PV Meter 3 IP", icon="mdi:ip-network"),
    "meter4_id": S("my-PV Meter 4 ID", icon="mdi:identifier"),
    "meter4_ip": S("my-PV Meter 4 IP", icon="mdi:ip-network"),
    "meter5_id": S("my-PV Meter 5 ID", icon="mdi:identifier"),
    "meter5_ip": S("my-PV Meter 5 IP", icon="mdi:ip-network"),
    "meter6_id": S("my-PV Meter 6 ID", icon="mdi:identifier"),
    "meter6_ip": S("my-PV Meter 6 IP", icon="mdi:ip-network"),
    "meter_ss": S("WiFi Meter Signalstärke", PERCENTAGE, "mdi:wifi"),
    "meter_ssid": S("meter_ssid", icon="mdi:wifi-marker"),
    "surplus": S(
        "Meter + Batterieladeleistung", UnitOfPower.WATT, "mdi:lightning-bolt"
    ),
    "m0sum": S("Hausanschluss", UnitOfPower.WATT, "mdi:transmission-tower"),
    "m0l1": S("Hausanschluss L1", UnitOfPower.WATT, "mdi:transmission-tower"),
    "m0l2": S("Hausanschluss L2", UnitOfPower.WATT, "mdi:transmission-tower"),
    "m0l3": S("Hausanschluss L3", UnitOfPower.WATT, "mdi:transmission-tower"),
    "m0bat": S("Batteriespeicher", UnitOfPower.WATT, "mdi:transmission-tower"),
    "m1sum": S("PV Leistung", UnitOfPower.WATT, "mdi:solar-power"),
    "m1l1": S("PV Leistung L1", UnitOfPower.WATT, "mdi:solar-power"),
    "m1l2": S("PV Leistung L2", UnitOfPower.WATT, "mdi:solar-power"),
    "m1l3": S("PV Leistung L3", UnitOfPower.WATT, "mdi:solar-power"),
    "m1devstate": S("PV Kommunikationsstatus", icon="mdi:link"),
    "m2sum": S("Batterie Leistung", UnitOfPower.WATT, "mdi:home-battery"),
    "m2l1": S("Batterie Leistung L1", UnitOfPower.WATT, "mdi:home-battery"),
    "m2l2": S("Batterie Leistung L2", UnitOfPower.WATT, "mdi:home-battery"),
    "m2l3": S("Batterie Leistung L3", UnitOfPower.WATT, "mdi:home-battery"),
    "m2soc": S("Batterie SoC", PERCENTAGE, "mdi:battery-charging-50"),
    "m2state": S("Batterie Status", icon="mdi:battery-heart-variant"),
    "m2devstate": S("Batterie Kommunikationsstatus", icon="mdi:link"),
    "m3sum": S("Ladestation Leistung", UnitOfPower.WATT, "mdi:ev-station"),
    "m3l1": S("Ladestation L1", UnitOfPower.WATT, "mdi:ev-station"),
    "m3l2": S("Ladestation L2", UnitOfPower.WATT, "mdi:ev-station"),
    "m3l3": S("Ladestation L2", UnitOfPower.WATT, "mdi:ev-station"),
    "m3soc": S("Ladestation SoC", PERCENTAGE, "mdi:battery-charging-50"),
    "m3devstate": S("Ladestation Kommunikationsstatus", icon="mdi:link"),
    "m4sum": S("Wärmepumpe Leistung", UnitOfPower.WATT, "mdi:heat-pump"),
    "m4l1": S("Wärmepumpe L1", UnitOfPower.WATT, "mdi:heat-pump"),
    "m4l2": S("Wärmepumpe L2", UnitOfPower.WATT, "mdi:heat-pump"),
    "m4l3": S("Wärmepumpe L3", UnitOfPower.WATT, "mdi:heat-pump"),
    "m4devstate": S("Wärmepumpe Kommunikationsstatus", icon="mdi:link"),
    "ecarstate": S("E-Auto Status", icon="mdi:car-electric"),
    "ecarboostctr": S("ecarboostctr"),
    "mss2": S("Sekundärregler 2 Status"),
    "mss3": S("Sekundärregler 3 Status"),
    "mss4": S("Sekundärregler 4 Status"),
    "mss5": S("Sekundärregler 5 Status"),
    "mss6": S("Sekundärregler 6 Status"),
    "mss7": S("Sekundärregler 7 Status"),
    "mss8": S("Sekundärregler 8 Status"),
    "mss9": S("Sekundärregler 9 Status"),
    "mss10": S("Sekundärregler 10 Status"),
    "mss11": S("Sekundärregler 11 Status"),
    "tempchip": S("tempchip", UnitOfTemperature.CELSIUS, "mdi:chip"),
    "volt_mains": S(
        "Eingangsspannung Leistungsteil L1",
        UnitOfElectricPotential.VOLT,
        "mdi:flash-triangle",
    ),
    "curr_mains": S("Current L1", UnitOfElectricCurrent.AMPERE, "mdi:current-ac"),
    "volt_L2": S(
        "Eingangsspannung Leistungsteil L2",
        UnitOfElectricPotential.VOLT,
        "mdi:flash-triangle",
    ),
    "curr_L2": S("Current L2", UnitOfElectricCurrent.AMPERE, "mdi:current-ac"),
    "volt_L3": S(
        "Eingangsspannung Leistungsteil L3",
        UnitOfElectricPotential.VOLT,
        "mdi:flash-triangle",
    ),
    "curr_L3": S("Current L3", UnitOfElectricCurrent.AMPERE, "mdi:current-ac"),
    "volt_out": S(
        "AusgangsspannungLeistungsteil",
        UnitOfElectricPotential.VOLT,
        "mdi:flash-triangle",
    ),
    "freq": S("Netzfrequenz", UnitOfFrequency.HERTZ, "mdi:sine-wave"),
    "temp_ps": S(
        "Temperatur Leistungsteil", UnitOfTemperature.CELSIUS, "mdi:thermometer"
    ),
    "fan_speed": S("Lüfterstufe", icon="mdi:fan"),
    "ps_state": S("Status Leistungsteil"),
    "cur_ip": S("IP", icon="mdi:ip-network"),
    "cur_sn": S("Serial number", icon="mdi:numeric"),
    "cur_gw": S("Gateway", icon="mdi:router-network"),
    "cur_dns": S("DNS"),
    "fwversionlatest": S("latest Firmware version", icon="mdi:numeric"),
    "psversionlatest": S("latest Power supply version", icon="mdi:numeric"),
    "p9sversionlatest": S("latest Power supply version Acthor 9", icon="mdi:numeric"),
    "upd_state": S("Update state", icon="mdi:update"),
    "upd_files_left": S("Update files left", icon="mdi:update"),
    "ps_upd_state": S("Power supply update state", icon="mdi:update"),
    "p9s_upd_state": S("Acthor 9 Power supply update state", icon="mdi:update"),
    "cloudstate": S("Cloud Status", icon="mdi:cloud-check"),
    "debug_ip": S("Debug IP", icon="mdi:ip-network"),
    # setup values
    "mainmode": S("Operating Mode", source="setup"),
    "mode9s": S("Operating Mode Acthor 9", source="setup"),
}
