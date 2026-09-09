# Name : Hernandez, Mart Darren I.
# Section : BMET 2101
# Task 4 : Temperature Check

name = input("Enter your name: ")
print("Hello, " + name)

temperature = float(input("Enter temperature in °C: "))

fahrenheit = temperature * 9 / 5 + 32
between = 20 <= temperature <= 30

print("Fahrenheit:", fahrenheit)
print("Between 20 and 30 °C:", between)