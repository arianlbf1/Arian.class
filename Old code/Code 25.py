import random
number=random.randint(1, 500)
attempts=0
max_attempts=30
while attempts<max_attempts:
    guess=int(input("Please enter a guess between 1-500:"))
    if attempts>max_attempts:
        print("You ran out of attempts.")
        break
    elif guess==number:
        print("Your guess was correct!")
        break
    elif guess<number:
        print("The number is bigger than your guess.")
    elif guess>number:
        print("The number is smaller than your guess.")
    else:
        ("Your guess was invalid, so the game has ended.")
        break