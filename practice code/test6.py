def calculate_cop(compressor_power, battery_capacity=0, battery_efficiency=1.0, average_irradiance=0):
  """
  Calculates the COP of a solar-powered refrigerator.

  Args:
      compressor_power (float): Average power consumption (W) of the refrigerator (excluding solar panel control system).
      battery_capacity (float, optional): Battery capacity (Ah). Defaults to 0.
      battery_efficiency (float, optional): Battery efficiency (decimal). Defaults to 1.0.
      average_irradiance (float, optional): Average solar irradiance (W/m^2). Defaults to 0.

  Returns:
      float: The COP value.
  """

  # Constants
  CP_AIR = 1006
  DENSITY_AIR = 1.225
  FRIDGE_VOLUME = 100 / 1000
  MEASUREMENT_PERIOD = 1800
  DESIRED_FRIDGE_TEMP = 6
  SOLAR_PANEL_AREA = 2
  SOLAR_PANEL_EFFICIENCY = 0.15
  INVERTER_EFFICIENCY = 1

  # Heat removal calculation
  delta_t = AMBIENT_TEMP - DESIRED_FRIDGE_TEMP
  mass_air = DENSITY_AIR * FRIDGE_VOLUME
  qcold_joules = CP_AIR * mass_air * delta_t * MEASUREMENT_PERIOD

  # Solar energy generation (excluding control system power)
  # You can modify this section to incorporate control system power consumption
  # based on manufacturer specifications or separate measurement (if feasible)
  solar_energy_generated_joules = average_irradiance * SOLAR_PANEL_AREA * MEASUREMENT_PERIOD * SOLAR_PANEL_EFFICIENCY

  # Battery storage
  available_energy_joules = solar_energy_generated_joules
  if battery_capacity > 0:
    battery_energy_joules = battery_capacity * 3600 * battery_efficiency
    available_energy_joules += battery_energy_joules

  # Adjusted compressor power consumption (can be modified to account for variations due to factors like door openings or temperature fluctuations)
  adjusted_compressor_power = compressor_power

  # Effective energy available after inverter losses
  effective_energy_joules = available_energy_joules * INVERTER_EFFICIENCY

  # COP calculation (addressing potential double-counting)
  total_energy_consumed_joules = adjusted_compressor_power * MEASUREMENT_PERIOD
  cop = qcold_joules / (total_energy_consumed_joules + effective_energy_joules)

  return cop


# User input
compressor_power = float(input("Enter average power consumption (W) excluding solar panel control system: "))
consider_ambient_temp = input("Account for ambient temperature? (y/n): ").lower()
AMBIENT_TEMP = float(input("Enter ambient temperature (°C): ")) if consider_ambient_temp == 'y' else 25
battery_capacity = float(input("Enter the battery capacity of your system (Ah) (optional, enter 0 if not applicable): "))
battery_efficiency = float(input("Enter the efficiency of your battery (decimal) (optional, enter 1 if not applicable): "))
average_irradiance = float(input("Enter the average solar irradiance for your location (W/m^2): "))

# Calculate COP
cop = calculate_cop(compressor_power, battery_capacity, battery_efficiency, average_irradiance)
print("COP of the solar-powered refrigerator:", cop)
