fruit = ["apple", "pear", "banana",  "lemon", "kiwi"]

# fruit_with_es = [f for f in fruit if "e" in f]
fruit_with_es = ["Has A" if "a" in f else "Not A" for f in fruit if "e" in f]

print(fruit_with_es)
