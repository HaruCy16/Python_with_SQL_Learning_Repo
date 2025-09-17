#CODE CONDITIONS, CHECKING FARE

print("WELCOME TO BUS TRANSPO")
print("Please enter your age:")
age = int(input())
fare = 0

FARE_CHILD = 5
FARE_TEEN = 7
FARE_ADULT = 10
FARE_SENIOR = 15

if age < 5:
    fare = FARE_CHILD
elif age <= 18:
    fare = FARE_TEEN
elif age <= 65:
    fare = FARE_ADULT
elif age > 66:
    fare = FARE_SENIOR
else:
    print("Invalid age entered.")

print(f"Your fare is: ${fare}")
print("Thank you for riding with us!\n")

#CODE CALCULATOR CONSOLE APP USING CONDITIONALS

print("WELCOME TO THE CALCULATOR APP")
print("Please enter the first number:")
num1 = float(input())
print("Please enter the second number:")
num2 = float(input())

print("Please enter the operation (+, -, *, /):")

operation = input()

result = 0

if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")

#LOOPS AND ITERATION, PRINT EVEN NUMBERS

print("\nEVEN NUMBER PRINTER")
print("Please enter a positive integer:")
n = int(input())

print(f"Even numbers from 1 to {n} are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
print("Thank you for using the Even Number Printer!\n")

#LOOPS AND ITERATION, PRINT MULTIPLICATION TABLE
print("\nMULTIPLICATION TABLE GENERATOR")
print("Please enter a positive integer:")

num = int(input())

print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
print("Thank you for using the Multiplication Table Generator!")