# 1. Your task is to create a Circle constructor that creates a circle with a
#     radius provided by an argument. The circles constructed must have two
#     instance methods: get_area() (πr^2) and get_circumference() (2πr)
#     which give both respective areas and circumference.
#    EXAMPLES:
#     circy = Circle(11)
#     circy.get_area()
#     Should return 380.132711084365

#     circy = Circle(4.44)
#     circy.get_circumference()
#     Should return 27.897342763877365


# 2. Create methods for the Calculator class that can do the following:
#    - Add two numbers
#    - Subtract two numbers
#    - Multiply two numbers
#    - Divide two numbers
#    EXAMPLES:
#     calculator = Calculator()
#     calculator.add(10, 5)  # => 15
#     calculator.subtract(10, 5)  # => 5
#     calculator.multiply(10, 5)  # => 50
#     calculator.divide(10, 5)  # => 2


# 3. Create a method in the Person class which returns how another person's
#     age compares. Given the objects p1, p2 and p3, which will be
#     initialised with the attributes name and age, return a sentence in
#     the following format:
#     {other_person} is {older than / younger than / the same age as} me.
#    EXAMPLES:
#     p1 = Person("Samuel", 24)
#     p2 = Person("Joel", 36)
#     p3 = Person("Lily", 24)
#     p1.compare_age(p2)  # => "Joel is older than me."
#     p2.compare_age(p1)  # => "Samuel is younger than me."
#     p1.compare_age(p3)  # => "Lily is the same age as me."


# 4. Create the instance attributes fullname, firstname, lastname and email
#     in an Employee class. Given a person's first and last names:
#    - Form the fullname by simply joining the first and last name together,
#       separated by a space.
#    - Form the email by joining the first and last name together with
#       a . in between, and follow it with @company.com at the end. Make
#       sure the entire email is in lowercase.
#    EXAMPLES:
#     emp_1 = Employee("John", "Smith")
#     emp_2 = Employee("Mary", "Sue")
#     emp_3 = Employee("Antony", "Walker")
#     emp_1.fullname  # => "John Smith"
#     emp_2.email  # => "mary.sue@company.com"
#     emp_3.firstname  # => "Antony"

# 5. Create a class that takes the following four arguments for a particular
#     football player:
#    - name
#    - age
#    - height
#    - weight
#     Also, create three instance methods for the class that returns the
#     following strings:
#    - get_age() returns "<name> is age <age>"
#    - get_height() returns "<name> is <height>cm"
#    - get_weight() returns "<name> weighs <weight>kg"
#    EXAMPLES:
#     p1 = Player("David Jones", 25, 175, 75)
#     p1.get_age()  # => "David Jones is age 25"
#     p1.get_height()  # => "David Jones is 175cm"
#     p1.get_weight()  # => "David Jones weighs 75kg"