import random 

computer = random.randint(0, 100)
guesses = 10

while not guesses == 0:
    guess = int(input("please enter a guess:"))
    if guess > computer:
        print("the number is lower")

    elif guess < computer:
        print("the number is higher")

    elif guess == computer:
        print("You got it right!")
        break
    
    else:
        print("ERROR")
        break

    guesses = guesses - 1

