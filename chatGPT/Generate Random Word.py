import random
import enchant
import string

def generate_valid_word(length):
    dictionary = enchant.Dict("en_US")
    letters = string.ascii_lowercase
    while True:
        word = ''.join(random.choice(letters) for _ in range(length))
        if dictionary.check(word):
            return word

random_word = generate_valid_word(5)
print(random_word)