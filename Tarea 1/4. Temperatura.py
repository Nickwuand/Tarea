def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) - 32

temperatura_celsius = float(input("Ingrese la temperatura en Celsius:"))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")