# Challenge: Write two functions with parameters
# Write each function underneath its instructions, then call it with the values given.

# 1. Write a function called add_numbers that prints the sum of the two numbers you pass in.
#    Call it a couple of times with different numbers.
#    Example output:
#    add_numbers(2, 3) prints 5
#    add_numbers(10, 45) prints 55


# 2. You've scrambled a word before: turn it into a list of letters, shuffle them, and
#    join them back together. Let's make that reusable. Write scramble(word) so it takes
#    any word and prints a scrambled version of it.
#    Example output:
#    scramble("python") might print nohtyp

def add_numbers(first, second):
    print(f"{first + second}")

def scramble(word):
    import random
    shuffle_word = list(word)
    random.shuffle(shuffle_word)
    print("".join(shuffle_word))

add_numbers(2, 3)
add_numbers(10, 34)
add_numbers(12, 10)
scramble("comida")
scramble("conejo")
scramble("python")