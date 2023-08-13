

wordle = "wider"
guess = "beret"
temp_wordle = ""

i = 0
w_index = ''
g_index = ''
green = ""
yellow = ""

loop = 5
y_loop = 5

while not loop == 0:
    w_index = wordle[i]
    g_index = guess[i]

    if w_index == g_index:
        green += "*"

        loop -= 1
        i += 1

    else:
        green += "@"

        loop -= 1
        i += 1

i = 0
loop = 5

print(green)

while not loop == 0:
    continue1 = True

    r_i = 0
    remove_index = green[i]

    i += 1

    if remove_index == '@':
        pass

    else:
        yellow += remove_index
        continue1 = False

    if not continue1:
        pass

    elif continue1:
        pass