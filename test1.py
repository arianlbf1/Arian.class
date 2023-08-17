

wordle = "wider"
temp_wordle = ""
guess = "beret"
temp_wordle = ""
empty = ""

i = 0
w_index = ''
g_index = ''
w1_i = 0
g1_i = 0
w1_index = 0
g1_index = 0 

green = ""
yellow = ""

loop = 5
loop1 = 5
loop2 = 6

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

        temp_wordle = wordle
        while not loop1 == 0:
            g1_i = guess[g1_index]

            while not loop2 == 0:
                if loop2 == 1:
                    yellow += "_"
                    break

                w1_i = temp_wordle[w1_index]

                if g1_i == w1_i:
                    temp_wordle = temp_wordle.replace(temp_wordle[w1_index], '')
                    print(temp_wordle)
                    yellow += "$"
                    w1_index += 1
                    break

                else:
                    w1_index += 1
                    
                loop2 -= 1

            g1_index += 1
            loop2 = len(temp_wordle)
            loop2 += 1
            loop1 -= 1
            w1_index = 0
    loop -= 0
print(yellow)