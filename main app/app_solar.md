# 🌞 Solar-Powered Refrigerator COP Calculator 🌡️

This Python script calculates the **Coefficient of Performance (COP)** of a solar-powered refrigerator. It evaluates the refrigerator's efficiency based on user inputs like compressor power, ambient temperature, battery capacity, battery efficiency, and solar irradiance.

## 📝 Parameters
- **Compressor Power (W):** Average power consumption of the refrigerator.
- **Ambient Temperature (°C):** The temperature of the surrounding environment.
- **Battery Capacity (Ah):** Capacity of the battery system.
- **Battery Efficiency (decimal):** Efficiency of the battery.
- **Average Solar Irradiance (W/m²):** Solar energy received per square meter.

## 📊 Formula
The script calculates COP using the formula:

\[ \text{COP} = \frac{Q_{\text{cold}}}{W_{\text{input}} + E_{\text{solar}}} \]

Where:
- \( Q_{\text{cold}} \) is the heat removed from the refrigerator space, calculated as:
  \[ Q_{\text{cold}} = C_p \times \text{mass\_air} \times \Delta T \times \text{MEASUREMENT\_PERIOD} \]
  - \( C_p \) is the specific heat capacity of air (1006 J/kg*K).
  - \(\text{mass\_air}\) is the mass of air inside the fridge.
  - \(\Delta T\) is the temperature difference between ambient and desired fridge temperature.
  - \(\text{MEASUREMENT\_PERIOD}\) is the time period for measurement (1800 seconds).

- \( W_{\text{input}} \) is the total energy consumed by the compressor:
  \[ W_{\text{input}} = \text{compressor\_power} \times \text{MEASUREMENT\_PERIOD} \]

- \( E_{\text{solar}} \) is the effective energy available from solar panels after accounting for battery storage and inverter losses:
  \[ E_{\text{solar}} = (\text{solar\_energy\_generated} + \text{battery\_energy}) \times \text{INVERTER\_EFFICIENCY} \]

## 🚀 How to Use
1. **Input Parameters:** Run the script and provide the required parameters when prompted.
2. **Calculate COP:** The script will compute the COP value and display it.

## 🔧 Installation
- Requires Python 3.x.
- No additional dependencies. Simply run the script!

