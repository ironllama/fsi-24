# 1. Remove all odd numbers in a given list using a lambda.

print("1: [34, 68, 98]:", list(filter(lambda x: x % 2 == 0, [34, 11, 23, 68, 98, 58473])))

# 2. Square every number in a given list of integers using a lambda.

print("2: [25, 64, 4, 49]:", list(map(lambda x: x**2, [5, 8, 2, 7])))
