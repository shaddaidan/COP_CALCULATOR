# Average specific heat capacities
CP_FOOD = 3.5  # kJ/kg*C (assumed average for various food items)
CP_AIR = 1.005  # kJ/kg*C

# Reasonable assumptions (modify if needed)
BATTERY_DISCHARGE_FACTOR = 0.9  # Assuming good quality battery
INVERTER_EFFICIENCY = 0.95  # Typical inverter efficiency
INSULATION_FACTOR = 0.8  # Represents reduced efficiency due to insulation (adjust for polystyrene)
AVERAGE_FRIDGE_OCCUPANCY = 0.7  # More realistic average occupancy by food (adjustable)

def calculate_cop(t_in, t_store, compressor_power, fridge_volume):
  """
  Calculates COP of a solar-powered fridge based on fridge volume.

  Args:
      t_in: Initial temperature of food (degrees Celsius).
      t_store: Storage temperature (desired cool temperature, degrees Celsius).
      compressor_power: Compressor power consumption (Watts).
      fridge_volume: Volume of the fridge (liters).

  Returns:
      COP (Coefficient of Performance) as a float.
  """

  # Estimated food volume based on average occupancy
  food_volume = fridge_volume * AVERAGE_FRIDGE_OCCUPANCY

  # Estimated food mass based on average density
  average_food_density = 1000 # kg/m^3 (assuming a general average)
  food_mass = food_volume / 1000 * average_food_density  # Convert liters to m^3

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
fridge_volume = float(input("Enter fridge volume (liters): "))

# Calculate and print COP
cop = calculate_cop(initial_temp, storage_temp, compressor_power, fridge_volume)
print("COP:", cop)
