# User input for fridge specific parameters
compressor_power = float(input("Enter the average power consumption of your refrigerator (Watts): "))

# User prompt for ambient temperature consideration
consider_ambient_temp = input("Do you want to account for ambient temperature (y/n)?: ").lower()

# Additional input for ambient temperature if chosen
if consider_ambient_temp == 'y':
    AMBIENT_TEMP = float(input("Enter the ambient temperature (°C): "))
else:
    AMBIENT_TEMP = 25  # Default value

def calculate_cop(compressor_power):
    """
    Calculates the COP (Coefficient of Performance) of a refrigerator.

    Args:
        compressor_power (float): Average power consumption of the compressor (Watts).
    Returns:
        float: The COP value of the refrigerator.
    """
    # Define constants (J/kg*K, kg/m^3, m^3, s, °C, °C)
    CP_AIR = 1006
    DENSITY_AIR = 1.225
    FRIDGE_VOLUME = 100 / 1000  # Volume of the refrigerator (m^3)
    MEASUREMENT_PERIOD = 86400  # Measurement period (seconds) in a day
    DESIRED_FRIDGE_TEMP = 4  # Desired temperature inside the fridge (Celsius)

    # Calculate theoretical heat removal (Qcold)
    delta_t = AMBIENT_TEMP - DESIRED_FRIDGE_TEMP  # Temperature difference

    mass_air = DENSITY_AIR * FRIDGE_VOLUME  # Mass of the air inside the fridge (kg)
    qcold_joules = CP_AIR * mass_air * delta_t * MEASUREMENT_PERIOD  # Heat removed in Joules

    # Calculate total energy consumed by the fridge (considering only compressor power)
    total_energy_consumed_joules = compressor_power * MEASUREMENT_PERIOD

    # Calculate COP
    cop = qcold_joules / total_energy_consumed_joules

    return cop

# Calculate and print COP
cop = calculate_cop(compressor_power)
print("COP of your refrigerator:", cop)
