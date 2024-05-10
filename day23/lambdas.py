# 1. Convert the following function to a lambda expression.
def exponentiate(base, exponent):
	return base ** exponent

print("1:", (lambda x, y: x ** y)(2, 3))


# 2. Create a lambda function that adds 15 to a given number passed in
#     as an argument.
print("2:", (lambda x: x + 15)(15))


# 3. Create a lambda function that multiplies argument x with argument y
#     and print the result.
print("3:", (lambda x, y: x * y)(2, 3))
