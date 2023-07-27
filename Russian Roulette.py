import random
import os
import time

def russian_roulette():
    done = False
    file = (input("Enter the path to your file:"))
    while not done:
        pc_number = random.randint(1, 6)
        print(pc_number)
        guess = int(input("Enter a number 1 to 6:"))

        print("The wheel is spinning.")
        time.sleep(2)
        print("The wheel is stopping")
        time.sleep(1)
        print("it flew past", random.randint(1, 6))
        time.sleep(1)
        print("its stopping but it passed", random.randint(1, 6))
        time.sleep(1)
        print("Oh no, its very close to", random.randint(1, 6))
        time.sleep(1)
        print("It landed on", pc_number)

        if guess == pc_number:
            print("You LOST.")
            os.remove(file)
            over = input("Would you like to continue? y/n")
            over = over.lower
             
            if over == 'n':
                print("Play again soon, bye.")
                done = True

            elif over == 'y':
                print("Okay.")

            else:
                print("ERROR")
            
        elif not guess == pc_number:
            over = input("Good guess, would you like to continue? y/n:")
            over = over.lower()

            if over == 'n':
                print("Play again soon, bye.")
                done = True

            elif over == 'y':
                print("Okay.")

            else:
                print("ERROR")

            

    
yes_no = input("This is Russian Roulette. Start game? y/n:")
yes_no = yes_no.lower()

if yes_no == 'n':
    print("Okay, bye.")

elif yes_no == 'y':
    russian_roulette()

else:
    print("ERROR")