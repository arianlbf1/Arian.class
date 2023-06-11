password = ""
i = 0
# finds 
def key_Encrypt(i,key):
    answer = ""
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>,./`~-_+=\|?/ "
    l = 0
    l = len(password)
    l_list = len(list)
    while key > l_list:
        key -= l_list
    while not l == 0:
        index = password[i]
        list_find = list.find(index) + key
        if list_find > l_list:
            list_find -= l_list
        answer += list[list_find]
        l -= 1
        i += 1
    print(answer)

def key_Decrypt(i, key):
    answer = ""
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>,./`~-_+=\|?/ "
    l = 0
    l = len(password)
    l_list = len(list)
    while key > l_list:
        key -= l_list
    while not l == 0:
        list_find = 0
        index = password[i]
        list_find = list.find(index) - key
        if list_find > l_list:
            list_find += l_list 
        answer += list[list_find]
        l -= 1
        i += 1
    print(answer)

while True:
    encrypt_decrypt = input("Do you want to Encrypt(E) or Decrypt(D) your password:")
    encrypt_decrypt = encrypt_decrypt.lower()
    if encrypt_decrypt == "e":
        password = input("What is the password you want to Encrypt?")
        key = int(input("Please enter the Key:"))
        key_Encrypt(i, key)
    elif encrypt_decrypt == "d":
        password = input("What is the password you want to Decrypt?")
        key = int(input("Please enter the Key:"))
        key_Decrypt(i, key)
    else: 
        print("ERROR")
    done = input("Do you want to continue y/n:")
    done = done.lower()
    if done == "n":
        print("Ok, have a nice day!")
        break
    elif done == "y":
        password = ""
        i = 0
        l = 0
        print("Nice!")
    else:
        print("ERROR")
        break
