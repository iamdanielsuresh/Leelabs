#!/usr/bin/env python3

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius
    
    Args:
        kelvin (float): Temperature in Kelvin
        
    Returns:
        float: Temperature in Celsius
    """
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Kelvin
    """
    return celsius + 273.15

def get_valid_temperature():
    """
    Get a valid temperature input from the user
    
    Returns:
        float: Valid temperature value
    """
    while True:
        try:
            temperature = float(input("Enter temperature value: "))
            return temperature
        except ValueError:
            print("Error: Please enter a valid number.")

def display_menu():
    """Display the temperature conversion menu"""
    print("\nTemperature Converter")
    print("-------------------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

def main():
    print("Temperature Converter")
    print("====================")
    print("Convert temperatures between Celsius, Fahrenheit, and Kelvin")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the Temperature Converter!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid option. Please try again.")
            continue
            
        # Get temperature from user
        if choice == '1':
            print("\n-- Celsius to Fahrenheit Conversion --")
            celsius = get_valid_temperature()
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
            
            # Add some useful reference points
            if celsius == 0:
                print("(Water freezes at 0°C or 32°F)")
            elif celsius == 100:
                print("(Water boils at 100°C or 212°F at sea level)")
                
        elif choice == '2':
            print("\n-- Fahrenheit to Celsius Conversion --")
            fahrenheit = get_valid_temperature()
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
            
            # Add some useful reference points
            if fahrenheit == 32:
                print("(Water freezes at 32°F or 0°C)")
            elif fahrenheit == 212:
                print("(Water boils at 212°F or 100°C at sea level)")
                
        elif choice == '3':
            print("\n-- Celsius to Kelvin Conversion --")
            celsius = get_valid_temperature()
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C = {kelvin:.2f}K")
            
            # Add some useful reference points
            if celsius == -273.15:
                print("(Absolute zero is -273.15°C or 0K)")
                
        elif choice == '4':
            print("\n-- Kelvin to Celsius Conversion --")
            kelvin = get_valid_temperature()
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K = {celsius:.2f}°C")
            
            # Add some useful reference points
            if kelvin == 0:
                print("(Absolute zero is 0K or -273.15°C)")
        
        # Pause to let user read the result
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()