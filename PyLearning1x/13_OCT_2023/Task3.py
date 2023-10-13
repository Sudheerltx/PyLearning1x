# 1. Use the ternary operator to find the maximum of three numbers entered by the user.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

tmp = (a if a > b else b)
ma = (tmp if tmp > c else c)
print("Maximum of ", a, b, c, "is", ma)

# 2. Develop a Python script that calculates the square and cube of a given number.
num = int(input("Enter a number:"))
print("Square of the number", num, "is", num**2)
print("Cube of the number", num, "is", num**3)