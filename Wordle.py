import random
import enchant
import string

guess_number = 5

print("This is wordle, * is green, - is yellow, and _ is gray.")

def generate_valid_word(length):
    dictionary = enchant.Dict("en_US")
    letters = string.ascii_lowercase
    while True:
        word = ''.join(random.choice(letters) for _ in range(length))
        if dictionary.check(word):
            return word

wordle = generate_valid_word(5)
print(wordle)

while not guess_number == 0:
    guess = input("Please enter your guess:")
    guess = guess.lower

    print()






























































