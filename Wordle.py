import random
import enchant
import string


guess_number = 5
valid_word = 1

print("This is wordle, * is green, $ is yellow, and _ is gray.")

def generate_valid_word(length):
    dictionary = enchant.Dict("en_US")
    letters = string.ascii_lowercase
    while True:
        word = ''.join(random.choice(letters) for _ in range(length))
        if dictionary.check(word):
            return word
        
def is_valid_word(guess, language="en_US"):
    dictionary = enchant.Dict(language)
    return dictionary.check(guess)

wordle = generate_valid_word(5)
print(wordle)

while not guess_number == 0:

    while not valid_word == 0:
        guess = input("Please enter your guess:")
        guess = guess.lower

        if is_valid_word(guess, language="en_US"):
            pass
        
        elif not is_valid_word(guess, language="en_US") or not len(guess) == 5:
            print("Your word is not valid, please enter another 5 letter word.")
    