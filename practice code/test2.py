# Define constants
DESIRED_FRIDGE_TEMP = 4  # Desired temperature inside the fridge (Celsius)

def calculate_cop(supplied_power_js, fridge_volume, ambient_temp, measurement_period):
  """
  Calculates the COP (Coefficient of Performance) of a solar-powered refrigerator based on user-supplied power in kJ/s and user-defined measurement period. However, this simplified version skips the conversion to Kelvin.

  Args:
      supplied_power_kjs (float): Power supplied to the refrigerator by the solar panel (kJ/s).
      fridge_volume (float): Volume of the refrigerator (cubic meters).
      ambient_temp (float): Ambient temperature (°C). (This value is assumed to be already in Celsius)
      measurement_period (float): Measurement period in seconds (user-defined).

  Returns:
      float: The COP value of the solar-powered refrigerator (based on simplified assumptions).
  """

  # Calculate heat removal required (consider ambient temperature)
  temperature_difference_celsius = ambient_temp - DESIRED_FRIDGE_TEMP

  # Convert power from J/s to Joules based on measurement period
  supplied_power_joules = supplied_power_js * measurement_period

  # Calculate theoretical heat removal (Qcold) (assuming constant temperature difference)
  mass_air = 1.289 * fridge_volume  # Assuming air density of 1.225 kg/m^3
  specific_heat_capacity = 1006  # Specific heat capacity of air (J/kg*K)
  heat_removal_joules = mass_air * specific_heat_capacity * temperature_difference_celsius * measurement_period

  # Calculate COP (efficiency)
  cop = heat_removal_joules / supplied_power_joules

  return cop

# User input for fridge volume, ambient temperature (Celsius), supplied power (kJ/s), and measurement period (seconds)
fridge_volume = float(input("Enter the volume of your refrigerator (cubic meters): "))
ambient_temp = float(input("Enter the ambient temperature (°C): "))  # Assuming Celsius input
supplied_power_kjs = float(input("Enter the power supplied to the fridge by the solar panel (kJ/s): "))
measurement_period = float(input("Enter the desired measurement period (seconds): "))

# Calculate COP
cop = calculate_cop(supplied_power_kjs, fridge_volume, ambient_temp, measurement_period)

# Print the result (clarifying the simplified assumptions)
print(f"COP of your solar-powered refrigerator (measured over {measurement_period} seconds, simplified model without Kelvin conversion): {cop:.2f}")
