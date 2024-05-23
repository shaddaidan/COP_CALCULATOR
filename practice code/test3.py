# Define constants
DESIRED_FRIDGE_TEMP = 4  # Desired temperature inside the fridge (Celsius)

def calculate_cop(supplied_power_kjs, fridge_volume, cooling_capacity_watts, temperature_difference_kelvin, measurement_period):
  """
  Calculates the COP (Coefficient of Performance) of a solar-powered refrigerator based on user-supplied power, cooling capacity, temperature difference, and measurement period.

  Args:
      supplied_power_kjs (float): Power supplied to the refrigerator by the solar panel (kJ/s).
      fridge_volume (float): Volume of the refrigerator (cubic meters) (not used in this version).
      cooling_capacity_watts (float): Cooling capacity of the evaporator in Watts.
      temperature_difference_kelvin (float): Temperature difference between desired fridge temperature and ambient temperature (in Kelvin).
      measurement_period (float): Measurement period in seconds (user-defined).

  Returns:
      float: The COP value of the solar-powered refrigerator.
  """

  # Convert power from kJ/s to Joules based on measurement period
  supplied_power_joules = supplied_power_kjs * measurement_period

  # Theoretical heat removal (considering supplied parameters)
  heat_removal_joules = cooling_capacity_watts * measurement_period

  # Calculate COP (efficiency)
  cop = heat_removal_joules / supplied_power_joules

  return cop

# User input for supplied power (kJ/s), cooling capacity (Watts), temperature difference (Kelvin), and measurement period (seconds)
supplied_power_kjs = float(input("Enter the power supplied to the fridge by the solar panel (kJ/s): "))
cooling_capacity_watts = float(input("Enter the cooling capacity of the evaporator (Watts): "))
temperature_difference_kelvin = float(input("Enter the temperature difference between desired fridge temperature and ambient temperature (Kelvin): "))
measurement_period = float(input("Enter the desired measurement period (seconds): "))

# Calculate COP
cop = calculate_cop(supplied_power_kjs, 0, cooling_capacity_watts, temperature_difference_kelvin, measurement_period)

# Print the result
print(f"COP of your solar-powered refrigerator (measured over {measurement_period} seconds): {cop:.2f}")
