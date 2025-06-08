FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert: "))
Celsius_or_Fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


if Celsius_or_Fahrenheit == "F".upper():
    fahrenheit = temperature
    print(f"{fahrenheit}°F is {convert_to_celsius(fahrenheit):.2f}°C")

elif Celsius_or_Fahrenheit == "C".upper():
    celsius = temperature
    print(f"{celsius}°C is {convert_to_fahrenheit(celsius):.2f}°F")