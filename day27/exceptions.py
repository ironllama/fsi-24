# print("STARTING")

# try:
#     with open('random-file-xyz.txt') as file:
#         read_data = file.read()
# except Exception as e:
#     print("You have a problem")
#     # print(type(e))
#     # print(e)

# print("DOING MORE STUFF")
# print("GOT TO THE END!")

print("START")
fruit = ["apple", "pear", "orange", "lemon", "kiwi"]

fav = 6

try:
    print(fruit[fav])
except ValueError as e:
    print(f"Not sure why you'd get this error")
except IndexError as e:
    print(f"{fav} doesn't exist. You're getting an {fruit[0]}.")

print("DONE")
