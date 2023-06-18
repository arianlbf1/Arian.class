import random
i = 0

def storeInformation():
    with open("passwords.txt", "a") as f:
        f.write(f"{id},{user_password}\n")

def readInformation(id):
    with open("passwords.txt", "r") as f:
        for line in f:
            stored_id, stored_password = line.strip().split(",")
        if stored_id == id:
            return stored_id , stored_password
        if stored_id != id:
            return print("Your username and password is incorrect.")

def enter_password(i, user_password):
    key = random.randint(0,1000)
    answer = ""
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>,./`~-_+=\|?/ "
    l = 0
    l = len(user_password)
    l_list = len(list)
    while key > l_list:
        key -= l_list
    while not l == 0:
        index = user_password[i]
        list_find = list.find(index) + key
        if list_find > l_list:
            list_find -= l_list
        answer += list[list_find]
        l -= 1
        i += 1
    print("Your key is", key)
    print(answer)

def enter_generated_password(i, generated_password):
    key = random.randint(0,1000)
    answer = ""
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>,./`~-_+=\|?/ "
    l = 0
    l = len(generated_password)
    l_list = len(list)
    while key > l_list:
        key -= l_list
    while not l == 0:
        index = generated_password[i]
        list_find = list.find(index) + key
        if list_find > l_list:
            list_find -= l_list
        answer += list[list_find]
        l -= 1
        i += 1
    print("Your key is", key)

def give_password(i, id_key):
    encrypted_password = readInformation(id)
    answer = ""
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>,./`~-_+=\|?/ "
    l = 0
    l = len(encrypted_password)
    l_list = len(list)
    while id_key > l_list:
        id_key -= l_list
    while not l == 0:
        list_find = 0
        index = encrypted_password[i]
        list_find = list.find(index) - id_key
        if list_find > l_list:
            list_find += l_list 
        answer += list[list_find]
        l -= 1
        i += 1
    print(answer)

def random_password(random_length):
    loop = 0
    generated_password = ''
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>,./`~-_+=\|?/ "
    while not loop == random_length:
        generated_password += list[random.randint(0,96)]
        loop += 1
    print("Your random password is", generated_password)
    print("Your password has been saved")
    return generated_password

while True:
    enter_get = input("Do you want to enter a password(E) or get a previous password back(G):")
    enter_get = enter_get.lower()

    if enter_get == 'e':
        generate_enter = input("Do you want to generate a password(G) or enter your own password(E):")
        generate_enter = generate_enter.lower()

        if generate_enter == 'g':
            random_length = int(input("Enter the best length for you password:"))
            generated_password = random_password(random_length)
            enter_generated_password(i, generated_password)

        elif generate_enter == 'e':
            user_password = input("Enter your password:")
            enter_password(i, user_password)

    elif enter_get == 'g':
        id = input("Enter your password ID:")
        id_key = input("Enter your password key:")
        give_password(i, id_key)

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