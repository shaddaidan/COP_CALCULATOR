# Average specific heat capacities
CP_FOOD = 3.5  # kJ/kg*C (assumed average for various food items)
CP_AIR = 1.005  # kJ/kg*C

# Reasonable assumptions (modify if needed)
BATTERY_DISCHARGE_FACTOR = 0.9  # Assuming good quality battery
INVERTER_EFFICIENCY = 0.95  # Typical inverter efficiency
INSULATION_FACTOR = 0.8  # Represents reduced efficiency due to insulation (adjust based on data)
AVERAGE_FRIDGE_OCCUPANCY = 0.7  # More realistic average occupancy by food (adjustable)
AVERAGE_FOOD_DENSITY = 750 # kg/m^3  # Between 800 and 900 kg/m^3 (adjustable)

def calculate_cop(t_in, t_store, compressor_power, fridge_volume):
  """
  Calculates COP, cooling capacity, and storage capacity of a solar-powered fridge.

  Args:
      t_in: Initial temperature of food (degrees Celsius).
      t_store: Storage temperature (desired cool temperature, degrees Celsius).
      compressor_power: Compressor power consumption (Watts).
      fridge_volume: Volume of the fridge (liters).

  Returns:
      A dictionary containing COP, cooling capacity, and storage capacity.
  """

  # Estimated food volume based on average occupancy
  food_volume = fridge_volume * AVERAGE_FRIDGE_OCCUPANCY

  # Estimated food mass based on average density
  food_mass = food_volume / 1000 * AVERAGE_FOOD_DENSITY  # Convert liters to m^3

  # Effective cooling efficiency considering insulation
  effective_cooling_efficiency = CP_AIR * INSULATION_FACTOR

  # Calculate COP
  cop = (food_mass * CP_FOOD + effective_cooling_efficiency * (t_in - t_store)) / (
      compressor_power * (1 / (BATTERY_DISCHARGE_FACTOR * INVERTER_EFFICIENCY))
  )

  # Cooling capacity (assuming specific heat of water for simplicity)
  cooling_capacity = food_mass * CP_FOOD * (t_in - t_store)  # J/cycle

  # Storage capacity (considering average occupancy)
  storage_capacity = fridge_volume * AVERAGE_FRIDGE_OCCUPANCY  # liters

  return {
      "COP": cop,
      "Cooling Capacity (J/cycle)": cooling_capacity,
      "Storage Capacity (liters)": storage_capacity
  }

# Get user input
initial_temp = float(input("Enter initial temperature of food (C): "))
storage_temp = float(input("Enter desired storage temperature (C): "))
compressor_power = float(input("Enter compressor power consumption (Watts): "))
fridge_volume = float(input("Enter fridge volume (liters): "))

# Calculate results
results = calculate_cop(initial_temp, storage_temp, compressor_power, fridge_volume)

# Print results in a formatted way
print("\n**Fridge Performance Analysis**")
print(f"  - Coefficient of Performance (COP): {results['COP']:.2f}")
print(f"  - Cooling Capacity: {results['Cooling Capacity (J/cycle)']:.2f} J/cycle")
print(f"  - Storage Capacity: {results['Storage Capacity (liters)']:.2f} liters")

