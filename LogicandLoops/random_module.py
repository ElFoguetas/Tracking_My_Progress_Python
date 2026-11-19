#Voy a utilziar los anagramas pasados para ver los usos del modulo random
import random

primer_anagrama = list("amor")
segundo_anagrama = list("roma")

# Mediante shuffle desordeno la lista original
random.shuffle(primer_anagrama)
random.shuffle(segundo_anagrama)

# Mediante choice voy a elegir un caracter al azar dentro de la lista
print(random.choice(primer_anagrama))
print(random.choice(segundo_anagrama))