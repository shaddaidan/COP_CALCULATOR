# Average specific heat capacities
CP_FOOD = 3.5  # kJ/kg*C (assumed average for various food items)
CP_AIR = 1.005  # kJ/kg*C

# Reasonable assumptions (modify if needed)
BATTERY_DISCHARGE_FACTOR = 0.9  # Assuming good quality battery
INVERTER_EFFICIENCY = 0.95  # Typical inverter efficiency
INSULATION_FACTOR = 0.8  # Represents reduced efficiency due to insulation (adjust based on data)

def calculate_cop(t_in, t_store, compressor_power, food_mass):
  """
  Calculates COP of a solar-powered fridge.

  Args:
      t_in: Initial temperature of food (degrees Celsius).
      t_store: Storage temperature (desired cool temperature, degrees Celsius).
      compressor_power: Compressor power consumption (Watts).
      food_mass: Mass of food inside the fridge (kg).

  Returns:
      COP (Coefficient of Performance) as a float.
  """

  # Effective cooling efficiency considering insulation
  effective_cooling_efficiency = CP_AIR * INSULATION_FACTOR

  # Calculate COP
  cop = (food_mass * CP_FOOD + effective_cooling_efficiency * (t_in - t_store)) / (
      compressor_power * (1 / (BATTERY_DISCHARGE_FACTOR * INVERTER_EFFICIENCY))
  )

  return cop

# Get user input
initial_temp = float(input("Enter initial temperature of food (C): "))
storage_temp = float(input("Enter desired storage temperature (C): "))
compressor_power = float(input("Enter compressor power consumption (Watts): "))
food_mass = float(input("Enter mass of food inside the fridge (kg): "))

# Calculate and print COP
cop = calculate_cop(initial_temp, storage_temp, compressor_power, food_mass)
print("COP:", cop)
