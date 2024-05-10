# x = 5
# y = 10

# def do_something(num):
#     global x, y
#     print("A:", x)
#     x = num
#     y = num

# do_something(43)
# print("B:", x, y)

# def create_adder(x):
#     def adder(y):
#         return x + y  # What happens to 'x' after 'create_adder' is done?
#     return adder

# add_10 = create_adder(10)
# print(add_10(3))
# print(add_10(8))
# print(add_10(1))
# print(add_10(100))
# print()

# add_100 = create_adder(100)
# print(add_100(12))
# print(add_100(21))
# print(add_100(988))
# print(add_100(34))

# def more_than_2(x):
#     return x > 2
# print(more_than_2(3))

# print((lambda x: x > 2)(3))

powers_of_2 = list(map(lambda x: 2 ** x, [1, 2, 3]))
print(powers_of_2)
