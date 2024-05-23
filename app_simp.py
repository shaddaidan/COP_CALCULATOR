# Define constants (replace with your actual values)
MEASUREMENT_PERIOD = 86400  # Measurement period (seconds) in a day
DESIRED_TEMP = 4  # °C (desired fridge temperature)
AMBIENT_TEMP = 25  # °C (ambient temperature)
SOLAR_PANEL_AREA = 2  # m^2 (area of the solar panel)
SOLAR_PANEL_EFFICIENCY = 0.15  # decimal (solar panel efficiency)
INVERTER_EFFICIENCY = 0.9  # decimal (inverter efficiency)
DUTY_CYCLE = 0.5  # Assumed duty cycle of the compressor (fraction of time it runs)

# User input
compressor_power = float(input("Enter the average power consumption of your refrigerator (Watts): "))
battery_capacity = float(input("Enter the battery capacity of your system (Ah) (optional, press Enter for 0): ")) or 0
battery_efficiency = float(input("Enter the efficiency of your battery (decimal) (optional, press Enter for 1): ")) or 1.0
average_irradiance = float(input("Enter the average solar irradiance for your location (W/m^2): ")) or 0

def calculate_cop(power, duty_cycle=DUTY_CYCLE):
  """Calculates energy consumption considering duty cycle.

  Args:
      power (float): Power consumption of the device (Watts).
      duty_cycle (float, optional): Duty cycle (fraction of time it runs). Defaults to 0.5.

  Returns:
      float: Energy consumption in Joules.
  """
  return power * MEASUREMENT_PERIOD * duty_cycle

# Calculate total energy consumed by the fridge
total_energy_joules = calculate_cop(compressor_power)

# Calculate estimated solar energy generation (assuming constant irradiance)
solar_energy_generated_joules = average_irradiance * SOLAR_PANEL_AREA * MEASUREMENT_PERIOD * SOLAR_PANEL_EFFICIENCY

# Account for battery storage (if applicable)
if battery_capacity > 0:
  battery_energy_joules = battery_capacity * 3600 * battery_efficiency
  available_energy_joules = (solar_energy_generated_joules + battery_energy_joules) * INVERTER_EFFICIENCY
else:
  available_energy_joules = solar_energy_generated_joules * INVERTER_EFFICIENCY

# Calculate COP (assuming cooling capacity equals compressor power)
if total_energy_joules > 0:
  COP = compressor_power / total_energy_joules
else:
  COP = 0

# Print the COP value
print("COP of your solar-powered refrigerator:", COP)
