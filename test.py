#stemp_wordle = temp_wordle.replace(temp_wordle[w1_index], '')

wordle = "wider"
temp_wordle = ""
guess = "berte" 
yellow = ""
green = ""
outcome = ""

l1 = 5
loop1 = 5
loop2 = 6
loop_n = 5

i = 0
w_i = 0
g_i = 0
w_index = 0
g_index = 0
y1_index = ""
g1_index = ""

l2 = 5

i1 = 0


temp_wordle = wordle
while not loop1 == 0:
    g_i = guess[g_index]

    while not loop2 == 0:
        if loop2 == 1:
            yellow += "_"
            break 
        w_i = temp_wordle[w_index]

        if g_i == w_i:
            temp_wordle = temp_wordle.replace(temp_wordle[w_index], '')
            print(temp_wordle)
            yellow += "$"
            w_index += 1
            break

        else:
            w_index += 1
            
        loop2 -= 1

    g_index += 1
    loop2 = len(temp_wordle)
    loop2 += 1
    loop1 -= 1
    w_index = 0

while not l1 == 0:
    gw_index = wordle[i]
    gg_index = guess[i]

    if gw_index == gg_index:
        green += "*"

        l1 -= 1
        i += 1

    else:
        green += "_"

        l1 -= 1
        i += 1

while not l2 == 0:
    y1_index = yellow[i1]
    g1_index = green[i1]

    if g1_index == "*":
        outcome += "*"
        
        l2 -= 1
        i1 += 1
    else:
        outcome += y1_index

        l2 -= 1
        i1 += 1
print(outcome)