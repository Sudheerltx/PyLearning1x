# Create a Program
# Take 5 numbers from the Users
# Add 1-2 duplicates
# print the non duplicate numbers

num_set = set()
for i in range(5):
    num = int(input("Enter a number : "))
    num_set.add(num)

print("Set of numbers :", num_set)
