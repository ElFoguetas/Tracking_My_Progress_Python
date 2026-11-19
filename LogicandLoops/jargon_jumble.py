# Challenge: Scramble a Word
# 1. Create a game file named `jargon_jumble.py`
# 2. Create a list of at least 3 words and save to a variable called `words`
# 3. Use random.choice() to pick a word from the list
# 4. Use list(), random.shuffle(), and "".join() to scramble the word
# 5. Print the scrambled word

import random # Importo el modulo de random

words = ["Market", "Values", "Anxious"] # hago mi lista de palabras
print(words) # prueba para ver la lista
word_list = list(random.choice(words)) # convierto a una lista para separar por caracteres una palabra elegida mediante el choice
random.shuffle(word_list) # Le doy un orden aleatorio a la palabra
shuffle_word = "".join(word_list) # Lo uno mediante la funcion Join para que sea un string de nuevo
print(shuffle_word) # Muestro la palabra