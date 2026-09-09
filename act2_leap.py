# Name : Hernandez, Mart Darren I.
# Section : BMET 2101
# Task 3 : Leap Year Test

name = input("Enter your name: ")
print("Hello, " + name)

year = int(input("Enter a year: "))

print((year % 4 == 0 and year % 100 != 0) or year % 100 == 0)