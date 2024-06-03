# Using classes
class Widget:
    def __init__(self, one, two, three=True):
        self.one = one
        self.two = two
        self.three = three

    def go(self):
        print(f"I am number {self.one}.")

    @property
    def two(self):
        return self._internal_two

    @two.setter
    def two(self, newVal):
        if isinstance(newVal, int):
            self._internal_two = newVal
        else:
            raise KeyError("BAD VAL. Must be an integer")

    @two.deleter
    def two(self):
        raise KeyError("Nope. This property is required.")

    def __repr__(self) -> str:
        return f"This is me: {{ one: {self.one}, two: {self.two}, three: {self.three} }}"

w1 = Widget("One", 1)
print("Object:", w1)
w1.go()

w2 = Widget("Two", 2, False)
w2.go()
w3 = Widget("Three", 3)
w3.go()
w4 = Widget("Four", 4)
w4.go()
w5 = Widget("Five", 5, False)
w5.go()

try:
    # w5.two = "2"  # Will raise a KeyError, because of custom checking we do
    del w5.two  # Will raise a KeyError, because of custom checking we do
except KeyError as e:
    print(e)

print("w5.two is now:", w5.two)
print()

# Using dictionaries
def go(d):
    print(f"I am number {d['one']}")

d1 = { "one": "Uno", "two": 1, "three": True }
print("Dict:", d1)
go(d1)

d2 = { "one": "Dos", "two": 2, "three": False }
go(d2)
d3 = { "one": "Tres", "two": 3, "three": True }
go(d3)
d4 = { "one": "Quattro", "two": 4, "three": True }
go(d4)
d5 = { "one": "Cinco", "two": 5, "three": False }
go(d5)
# d5['two'] = "2"  # Allowed
# del d5['two']  # Allowed, will cause error in next print line
print("d5['two'] is now:", d5['two'])
print()

# Named Tuples
from collections import namedtuple

Sprocket = namedtuple('Sprocket', ['one', 'two', 'three'])
def tgo(t):
    print(f"I am number {t.one}, or {t[0]}")

s1 = Sprocket('Ein', 1, True)
print("NTup:", s1)
tgo(s1)

s2 = Sprocket('Zwei', 2, False)
tgo(s2)
s3 = Sprocket('Drei', 3, False)
tgo(s3)
s4 = Sprocket('Vier', 4, False)
tgo(s4)
s5 = Sprocket('Fünf', 5, True)
tgo(s5)
# s5.two = 2  # Can't change -- tuples are immutable
# del s5.two  # Can't delete -- tuples are immutable
