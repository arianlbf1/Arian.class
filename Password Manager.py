import pyperclip
import random 

def enter_password():
    print("TEST")

def get_password():
    print("TEST")

def random_password():
    print("TEST")

while True:
    enter_get = input("Do you want to enter a password(E) or get a previous password back(G):")
    enter_get = enter_get.lower()
    if enter_get == 'e':
        generate_enter = input("Do you want to generate a password(G) or enter your own password(E):")
        generate_enter = generate_enter.lower()
        if generate_enter == 'g':
            random_password()
        elif generate_enter == 'e':
            user_password = input("Enter your password:")
            enter_password()
    elif enter_get == 'g':
        id = input("Enter your password ID:")
        id_key = input("Enter your password key:")
        get_password()
    else:
        print("ERROR")
    done = input("Do you want to continue y/n:")
    done = done.lower()
    if done == 'y':
        print("Nice!")
        enter_get = ''
        generate_enter = ''
        user_password = ""
        id = ""
        id_key = ""
    elif done == 'n':
        print("Ok, have a nice day!")
        break
    else:
        print("ERROR")
        break

