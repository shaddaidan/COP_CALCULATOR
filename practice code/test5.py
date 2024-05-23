# User input for fridge specific parameters
compressor_power = float(input("Enter the average power consumption of your refrigerator compressor (Watts): "))

# User prompt for ambient temperature consideration
consider_ambient_temp = input("Do you want to account for ambient temperature (y/n)?: ").lower()

# Additional input for ambient temperature if chosen
if consider_ambient_temp == 'y':
  AMBIENT_TEMP = float(input("Enter the ambient temperature (°C): "))
else:
  AMBIENT_TEMP = 25  # Default value

# User input for door opening frequency
door_openings_per_day = float(input("Enter the estimated number of door openings per day: "))

def calculate_cop(compressor_power, ambient_temp, door_openings_per_day):
  """
  Calculates a more refined estimate of the COP (Coefficient of Performance) of a refrigerator.

  Args:
      compressor_power (float): Average power consumption of the compressor (Watts).
      ambient_temp (float): Ambient temperature (°C).
      door_openings_per_day (float): Estimated number of door openings per day.

  Returns:
      float: The estimated COP value of the refrigerator.
  """

  # Define constants
  CP_AIR = 1006  # Specific heat capacity of air (J/kg*K)
  DENSITY_AIR = 1.225  # Air density (kg/m^3)
  FRIDGE_VOLUME = 0.1  # Adjust as needed based on your refrigerator volume (m^3)
  MEASUREMENT_PERIOD = 86400  # Measurement period (seconds) in a day

  # Desired fridge temperature (Celsius)
  DESIRED_FRIDGE_TEMP = 4

  # Heat gain due to door openings (simplified calculation)
  # Assuming each opening introduces a fixed amount of warm air
  # Consider revising this based on data or studies
  heat_gain_openings = door_openings_per_day * 1000  # Adjust the constant based on research

  # Calculate theoretical heat removal (Qcold)
  delta_t = AMBIENT_TEMP - DESIRED_FRIDGE_TEMP  # Temperature difference

  mass_air = DENSITY_AIR * FRIDGE_VOLUME  # Mass of the air inside the fridge (kg)
  qcold_joules = CP_AIR * mass_air * delta_t * MEASUREMENT_PERIOD + heat_gain_openings

  # Calculate total energy consumed by the fridge (considering only compressor power)
  total_energy_consumed_joules = compressor_power * MEASUREMENT_PERIOD

  # Calculate COP
  cop = qcold_joules / total_energy_consumed_joules

  return cop

# Calculate and print COP
cop = calculate_cop(compressor_power, AMBIENT_TEMP, door_openings_per_day)
print("Estimated COP of your refrigerator:", cop)
