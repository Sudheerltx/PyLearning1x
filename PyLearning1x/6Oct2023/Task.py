# Program to print tables without using loops
n = int(input('Enter number\n'))

print(f'Table of {n} is : ')

print(f'{n} X 1 = {n*1}')
print(f'{n} X 2 = {n*2}')
print(f'{n} X 3 = {n*3}')
print(f'{n} X 4 = {n*4}')
print(f'{n} X 5 = {n*5}')
print(f'{n} X 6 = {n*6}')
print(f'{n} X 7 = {n*7}')
print(f'{n} X 8 = {n*8}')
print(f'{n} X 9 = {n*9}')
print(f'{n} X 10 = {n*10}')

# ----------------Another way of doing the same ------------------------
# 2*1 = 2
# 2*2 = 4
# ....
# 2*10 = 20

# String.format
""" 
row1 = "2x1={}".format(2*1)
row2 = "2x2={}".format(2*2)
row3 = "2x3={}".format(2*3)
row4 = "2x4={}".format(2*4)
row5 = "2x5={}".format(2*5)
row6 = "2x6={}".format(2*6)
row7 = "2x7={}".format(2*7)
row8 = "2x8={}".format(2*8)
row9 = "2x9={}".format(2*9)
row10 = "2x10={}".format(2*10)
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)
print(row7)
print(row8)
print(row9)
print(row10)
"""
