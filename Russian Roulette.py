import random
import os
import time

def russian_roulette():
    done = False

    while not done:
        pc_number = random.randint(1, 6)
        print(pc_number)
        guess = int(input("Enter a number 1 to 6:"))

        print("Checking guess.")
        time.sleep(5)

        if guess == pc_number:
            print("Wrong number, you LOST.")
            os.remove(r"file.png")

        elif not guess == pc_number:
            over = input("Good guess, would you like to continue? y/n:")
            over = over.lower()

            if over == 'y':
                print("Play again soon, bye.")
                done = True

            elif over == 'n':
                print("Feeling lucky, okay.")

            else:
                print("ERROR")

            

    
yes_no = input("This is Russian Roulette, put a path to a cared file where it says r\"put file herer\". Are you sure that you want to play? y/n:")
yes_no = yes_no.lower()

if yes_no == 'n':
    print("Okay, bye.")

elif yes_no == 'y':
    print("Lets start.")
    russian_roulette()

else:
    print("ERROR")