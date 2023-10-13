# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
r = int(input("Enter the radius of the circle:"))
pi = (22/7)
area = pi * r * r
print(" Area of the circle is :", area)
area2 = pi * (r**2)  # Used exponential operator
print(" Area2 of the circle is :", area2)

# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num1, " is lesser than ", num2)
else:
    print(num1, " is equal to ", num2)