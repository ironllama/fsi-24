# 1. A pair of strings form a strange pair if both of the following are true:
#    - The 1st string's first letter = 2nd string's last letter.
#    - The 1st string's last letter = 2nd string's first letter.
#     Create a function that returns True if a pair of strings constitutes
#     a strange pair, and False otherwise.
#    EXAMPLES:
#     is_strange_pair("ratio", "orator")  # => True
#     is_strange_pair("sparkling", "groups")  # => True
#     is_strange_pair("bush", "hubris")  # => False
#     is_strange_pair("", "")  # => True


# 2. Create a function that accepts a string as an argument and returns the
#     first non-repeated character. Return False if all characters repeat
#     or if a blank string is provided.
#    EXAMPLES:
#     first_nrc("g")  # => "g"
#     first_nrc("it was then the frothy word met the round night")  # => "a"
#     first_nrc("the quick brown fox jumps then quickly blows air")  # => "f"
#     first_nrc("hheelloo")  # => False
#     first_nrc("")  # => False


# 3. Create a function that takes a phrase and transforms each word using the
#     following rules:
#    - Keep first and last character the same.
#    - Transform middle characters into a dash -.
#    - Words with two or fewer letters should not be hidden at all.
#    EXAMPLES:
#     ltr_hide("skies were pretty")  # => "s---s w--e p----y"
#     ltr_hide("red is not my color")  # => "r-d is n-t my c---r"
#     ltr_hide("She rolled her eyes")  # => "S-e r----d h-r e--s"

#     ltr_hide("Harry went to fight the basilisk")
#     Outputs:
#      "H---y w--t to f---t t-e b------k"


# 4. Create a function that counts the number of towers.
#    EXAMPLES:
#     count_towers([
#       ["     ##         "],
#       ["##   ##        ##"],
#       ["##   ##   ##   ##"],
#       ["##   ##   ##   ##"]
#     ])  # => 4
#     count_towers([
#       ["                         ##"],
#       ["##             ##   ##   ##"],
#       ["##        ##   ##   ##   ##"],
#       ["##   ##   ##   ##   ##   ##"]
#     ])  # => 6
#     count_towers([
#       ["##"],
#       ["##"]
#     ])  # => 1


# 5. Given a list of integers, find the pair of adjacent elements that have
#     the largest product and return that product.
#    EXAMPLES:
#     adjacent_product([3, 6, -2, -5, 7, 3])  # => 21
#     adjacent_product([5, 6, -4, 2, 3, 2, -23])  # => 30
#     adjacent_product([0, -1, 1, 24, 1, -4, 8, 10])  # => 80


# 6. You are to read each part of the date into its own integer type variable.
#     The year should be a 4 digit number. You can assume the user enters a
#     correct date (no error checking required). Determine whether the
#     entered date is a magic date. Here are the rules for a magic date:
#    - mm * dd is a 1-digit number that matches the last digit of yyyy or
#    - mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
#    - mm * dd is a 3-digit number that matches the last 3 digits of yyyy
#     The program should then display True if the date is magic, or
#     False if it is not.
#    EXAMPLES:
#     magic("1 1 2011")  # => True
#     magic("4 1 2001")  # => False
#     magic("5 2 2010")  # => True
#     magic("9 2 2011")  # => False
