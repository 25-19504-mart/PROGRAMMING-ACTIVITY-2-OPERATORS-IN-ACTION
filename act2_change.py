# Name = Hernandez, Mart Darren I.
# Section = BMET 2101
# Task 1 = Change Calculator

name = input("Enter your name: ")
print("Hello, " + name)

money = int(input("Enter amount in pesos: "))
print(money // 100)    

hundreds = money // 100
remainder = money % 100

twenties = remainder // 20
remainder = remainder % 20

fives = remainder // 5
remainder = remainder % 5

ones = remainder // 1
remainder = remainder % 1

print("100 pesos:", hundreds)
print("20 pesos:", twenties)
print("5 pesos:", fives)
print("1 peso:", ones)