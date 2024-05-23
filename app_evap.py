# COP calculator for solar-powered refrigerators

# User input for fridge specific parameters
compressor_power = float(input("Enter the average power consumption of your refrigerator (Watts): "))

# User input for optional solar related parameters (press Enter for default values)
battery_capacity = float(input("Enter the battery capacity of your system (Ah) (optional, press Enter for 0): ")) or 0
battery_efficiency = float(input("Enter the efficiency of your battery (decimal) (optional, press Enter for 1.0): ")) or 1.0
average_irradiance = float(input("Enter the average solar irradiance for your location (W/m^2) (optional, press Enter for 0): ")) or 0

def calculate_cop(compressor_power, battery_capacity=0, battery_efficiency=1.0, average_irradiance=0):
  """
  Calculates the COP (Coefficient of Performance) of a solar-powered refrigerator.

  Args:
      compressor_power (float): Average power consumption of the refrigerator (Watts).
      battery_capacity (float, optional): Battery capacity of the system (Ah). Defaults to 0.
      battery_efficiency (float, optional): Efficiency of the battery (decimal). Defaults to 1.0.
      average_irradiance (float, optional): Average solar irradiance for the location (W/m^2). Defaults to 0.

  Returns:
      float: The COP value of the solar-powered refrigerator.
  """

  # Constants (modify if needed)
  MEASUREMENT_PERIOD = 86400  # Measurement period (seconds) in a day
  DESIRED_FRIDGE_TEMP = 4  # Desired temperature inside the fridge (Celsius)
  AMBIENT_TEMP = 25  # Ambient temperature (Celsius)
  SOLAR_PANEL_AREA = 2  # Area of the solar panel (square meters)
  SOLAR_PANEL_EFFICIENCY = 0.15  # Solar panel efficiency (decimal)
  INVERTER_EFFICIENCY = 0.9  # Inverter efficiency (decimal)

  # Calculate theoretical heat removal (Qcold)
  delta_t = AMBIENT_TEMP - DESIRED_FRIDGE_TEMP  # Temperature difference
  qcold_joules = 1006 * 1.225 * DESIRED_FRIDGE_TEMP * delta_t * MEASUREMENT_PERIOD  # Pre-calculated for efficiency

  # Calculate total energy consumed by the fridge
  total_energy_consumed_joules = compressor_power * MEASUREMENT_PERIOD

  # Check for zero energy consumption (error handling)
  if total_energy_consumed_joules <= 0:
    print("Error: Fridge might not be consuming any energy. Check measurements.")
    return 0

  # Calculate estimated solar energy generation (assuming constant irradiance)
  solar_energy_generated_joules = average_irradiance * SOLAR_PANEL_AREA * MEASUREMENT_PERIOD * SOLAR_PANEL_EFFICIENCY

  # No battery case (directly calculate available energy)
  available_energy_joules = solar_energy_generated_joules

  # Calculate effective energy available after inverter losses
  effective_energy_joules = available_energy_joules * INVERTER_EFFICIENCY

  # Calculate COP
  cop = qcold_joules / total_energy_consumed_joules

  return cop

# Test 1: No battery, moderate solar irradiance
print("Test 1: No Battery, Moderate Solar Irradiance")
cop = calculate_cop(100, 0, 1.0, 4)  # 100W compressor, 4 kWh/m²/day solar irradiance
print("COP:", cop)

# Test 2: Battery present, high solar irradiance
print("\nTest 2: Battery Present, High Solar Irradiance")
cop = calculate_cop(150, 200, 0.9, 6)  # 150W compressor, 200Ah battery, 6 kWh/m²/day solar irradiance
print("COP:", cop)
