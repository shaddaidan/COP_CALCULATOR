# COP calculator for solar-powered refrigerators

# User input for fridge specific parameters
compressor_power = float(input("Enter the average power consumption of your refrigerator (Watts): "))

# User prompt for ambient temperature consideration
consider_ambient_temp = input("Do you want to account for ambient temperature (y/n)?: ").lower()

# Additional input for ambient temperature if chosen
if consider_ambient_temp == 'y':
  ambient_temp = float(input("Enter the ambient temperature (°C): "))
else:
  ambient_temp = 25  # Default value (unchanged from previous version)

battery_capacity = float(input("Enter the battery capacity of your system (Ah) (optional, enter 0 if not applicable): "))
battery_efficiency = float(input("Enter the efficiency of your battery (decimal) (optional, enter 1 if not applicable): "))
average_irradiance = float(input("Enter the average solar irradiance for your location (W/m^2): "))


# Define constants (J/kg*K, kg/m^3, m^3, s, °C, °C, m², %, %)
CP_AIR = 1006
DENSITY_AIR = 1.225
FRIDGE_VOLUME = 100 / 1000  # Volume of the refrigerator (m^3)
MEASUREMENT_PERIOD = 86400  # Measurement period (seconds) in a day
DESIRED_FRIDGE_TEMP = 4  # Desired temperature inside the fridge (Celsius)
SOLAR_PANEL_AREA = 2  # Area of the solar panel (square meters)
SOLAR_PANEL_EFFICIENCY = 0.15  # Solar panel efficiency (decimal)
INVERTER_EFFICIENCY = 0.9  # Inverter efficiency (decimal)


def calculate_cop(compressor_power, battery_capacity=0, battery_efficiency=1.0, average_irradiance=0, ambient_temp=25):
  """
  Calculates the COP (Coefficient of Performance) of a solar-powered refrigerator.

  Args:
      compressor_power (float): Average power consumption of the refrigerator (Watts).
      battery_capacity (float, optional): Battery capacity of the system (Ah). Defaults to 0.
      battery_efficiency (float, optional): Efficiency of the battery (decimal). Defaults to 1.0.
      average_irradiance (float, optional): Average solar irradiance for the location (W/m^2). Defaults to 0.
      ambient_temp (float, optional): Ambient temperature (°C). Defaults to 25.

  Returns:
      float: The COP value of the solar-powered refrigerator.
  """

  # Calculate theoretical heat removal (Qcold)
  delta_t = ambient_temp - DESIRED_FRIDGE_TEMP  # Temperature difference

  mass_air = DENSITY_AIR * FRIDGE_VOLUME  # Mass of the air inside the fridge (kg)
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

# Calculate and print COP
cop = calculate_cop(compressor_power, battery_capacity, battery_efficiency, average_irradiance, ambient_temp)
print("COP of your solar-powered refrigerator:", cop)
