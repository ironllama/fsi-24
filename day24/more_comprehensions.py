# Generate your own lists of numbers, sentences, and strings for these
#  exercises and use several permutations to verify that they work
#  as intended!

# 1. Given a list of numbers, write a list comprehension that produces a
#     list of strings of each number that is divisible by 5.

# 2. Given a sentence, produce a list of the lengths of each word in the
#     sentence, but only if the word is not 'the'.

# 3. Given a string representing a word, write a list comprehension that
#     produces a list of all the vowels in that word.

# 4. Given a string representing a word, write a set comprehension that
#     produces a set of all the vowels in that word.

# 5. Given a sentence, return the sentence with all vowels removed.

# 6. Given a list of numbers, return the list with all even numbers doubled,
#     and all odd numbers turned negative.

# 7. Given a sentence, return a new sentence with all its letters transposed
#     by 1 letter right in the alphabet, but only if the new letter is
#     between b and y, inclusive.
sentence = "Carry out a random act of kindness, with no expectation of reward, safe in the knowledge that one day someone might do the same for you."
alphas = "abcdefghijklmnopqrstuvwxy"
print("".join([alphas[alphas.find(letter) + 1] if letter in alphas and letter != "y" else letter for letter in sentence.lower()]))

# 8. Given a list of floats and ints, remove the floats (numbers with decimals).