from random import randint

# 1. Sort this list of people by age in ascending order without
#     changing the list.
people = [
  {'name': 'Jim', 'salary': 1_000, 'age': 30},
  {'name': 'Bob', 'salary': 2_000, 'age': 260},
  {'name': 'Anne', 'salary': 3_000, 'age': 123},
]

sorted_by_age = sorted(people, key=lambda person: person['age'])
print("1a:", sorted_by_age)

#    b. Sort by salary in descending order without changing the list.
sorted_by_salary = sorted(people, key=lambda person: person['salary'], reverse=True)
print("1b:", sorted_by_salary)

#    c. Sort by their names in ascending order in a way that
#        modifies the list.
people.sort(key=lambda person: person['name'])
print("1c:", people)
print()

# 2. Fill in the missing items in the constructor for the following class.
class Monster:
  def __init__(self, speed, height, health):
    self.speed = speed
    self.height = height
    self.health = health
    # pass  # Delete me!
    # Fill in here!
  
  # Special dunder function used when converting this object into a string
  # For example, when printing. This function will be called.
  # Similar to __str__, too. You can think of the two as:
  # __repr__ for developers (debugging or logging)
  # __str__ for users (UI and reports)
  def __repr__(self):
    desc = f'Monster: speed->{self.speed}, '
    desc += f'height->{self.height}, '
    desc += f'health->{self.health}, '
    return desc

m1 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m2 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m3 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m4 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))

monsters = [m1, m2, m3, m4]
print("2a:", monsters)
#    b. Sort this list of monsters by speed in ascending order without
#        changing the list.
print("2b", sorted(monsters, key=lambda m: m.speed))

#    c. Sort this list of monsters by height in descending order
#        without changing the list.
print("2c", sorted(monsters, key=lambda m: m.height, reverse=True))

#    d. Sort this list of monsters by health in ascending order
#        without changing the list.
print("2d", sorted(monsters, key=lambda m: m.health))

#    e. Sort this list of monsters by their health x height in
#        ascending order and modify the original list.
for m in monsters:
  m.hxh = m.health * m.height

monsters.sort(key=lambda m: m.hxh)
print("2e", "\n".join([str(m) for m in monsters]))
