import random

def salt_origin():
    loop = 0
    generated_password = ''
    list = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]:;'\"<>.`~-_+=\|?/"
    len_list = len(list)
    while not loop == 28:
        generated_password += list[random.randint(0, len_list)]
        loop += 1
    return generated_password

def salt_round():
    i = random.randit[0, 100]


def gensalt(rounds, password):
    rounds = int(input("How many rounds?"))