def calculate_cop(cooling_capacity_btu_hr, compressor_power_w):
    # Convert cooling capacity from BTU/hr to watts
    cooling_capacity_w = cooling_capacity_btu_hr / 3.412
    
    # Calculate COP
    cop = cooling_capacity_w / compressor_power_w
    
    return cop

def main():
    # Collect user input
    try:
        cooling_capacity_btu_hr = float(input("Enter the cooling capacity (in BTU/hr): "))
        compressor_power_w = float(input("Enter the power consumption of the compressor (in watts): "))
        
        # Calculate COP
        cop = calculate_cop(cooling_capacity_btu_hr, compressor_power_w)
        
        # Print the result
        print(f"The Coefficient of Performance (COP) of the refrigerator is: {cop:.2f}")
    
    except ValueError:
        print("Please enter valid numerical values for the cooling capacity and compressor power.")

if __name__ == "__main__":
    main()
