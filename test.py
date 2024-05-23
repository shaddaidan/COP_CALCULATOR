# Define constants (J/kg*K, kg/m^3, s, °C, °C, m², %, %)
CP_AIR = 1006
DENSITY_AIR = 1.225
MEASUREMENT_PERIOD = 86400  # Measurement period (seconds) in a day
DESIRED_FRIDGE_TEMP = 4  # Desired temperature inside the fridge (Celsius)
SOLAR_PANEL_AREA = 2  # Area of the solar panel (square meters)
SOLAR_PANEL_EFFICIENCY = 0.15  # Solar panel efficiency (decimal)
INVERTER_EFFICIENCY = 0.9  # Inverter efficiency (decimal)

def calculate_cop(compressor_power, fridge_volume, battery_capacity=0, battery_efficiency=1.0, average_irradiance=0, ambient_temp=25):
    """
    Calculates the COP (Coefficient of Performance) of a solar-powered refrigerator.

    Args:
        compressor_power (float): Average power consumption of the refrigerator (Watts).
        fridge_volume (float): Volume of the refrigerator (cubic meters).
        battery_capacity (float, optional): Battery capacity of the system (Ah). Defaults to 0.
        battery_efficiency (float, optional): Efficiency of the battery (decimal). Defaults to 1.0.
        average_irradiance (float, optional): Average solar irradiance for the location (W/m^2). Defaults to 0.
        ambient_temp (float, optional): Ambient temperature (°C). Defaults to 25.

    Returns:
        float: The COP value of the solar-powered refrigerator.
    """
    
    # Calculate theoretical heat removal (Qcold)
    delta_t = ambient_temp - DESIRED_FRIDGE_TEMP  # Temperature difference

    # Convert temperature difference to Kelvin
    # delta_t_kelvin = delta_t + 273.15
    # delta_t = AMBIENT_TEMP - DESIRED_FRIDGE_TEMP 

    mass_air = DENSITY_AIR * fridge_volume  # Mass of the air inside the fridge (kg)
    # qcold_joules = CP_AIR * mass_air * delta_t_kelvin * MEASUREMENT_PERIOD 

    qcold_joules = CP_AIR * mass_air * delta_t * MEASUREMENT_PERIOD  # Heat removed in Joules

    # Calculate total energy consumed by the fridge
    total_energy_consumed_joules = compressor_power * MEASUREMENT_PERIOD


    

    # Check for zero energy consumption (error handling)
    if total_energy_consumed_joules <= 0:
        print("Error: Fridge might not be consuming any energy. Check measurements.")
        return 0

    # Calculate estimated solar energy generation (assuming constant irradiance)
    solar_energy_generated_joules = average_irradiance * SOLAR_PANEL_AREA * MEASUREMENT_PERIOD * SOLAR_PANEL_EFFICIENCY

    # Account for battery storage (if applicable)
    available_energy_joules = solar_energy_generated_joules
    if battery_capacity > 0:
        battery_energy_joules = battery_capacity * 3600 * battery_efficiency
        available_energy_joules += battery_energy_joules

    # Calculate effective energy available after inverter losses
    effective_energy_joules = available_energy_joules * INVERTER_EFFICIENCY

    # Calculate COP
    cop = qcold_joules / total_energy_consumed_joules

    return cop

# Test cases with fridge volume added
test_cases = [
    {"compressor_power": 100, "fridge_volume": 0.1, "AMBIENT_TEMP": 30, "battery_capacity": 100, "battery_efficiency": 0.9, "average_irradiance": 500},
    {"compressor_power": 200, "fridge_volume": 0.15, "AMBIENT_TEMP": 25, "battery_capacity": 200, "battery_efficiency": 0.95, "average_irradiance": 700},
    {"compressor_power": 150, "fridge_volume": 0.2, "AMBIENT_TEMP": 35, "battery_capacity": 0, "battery_efficiency": 1.0, "average_irradiance": 600},
]

for idx, test in enumerate(test_cases):
    cop = calculate_cop(test["compressor_power"], test["fridge_volume"], test["battery_capacity"], test["battery_efficiency"], test["average_irradiance"], test["AMBIENT_TEMP"])
    print(f"Test Case {idx + 1} - COP of your solar-powered refrigerator: {cop:.2f}")
