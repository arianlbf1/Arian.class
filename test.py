wordle = "wider"
temp_wordle = ""
guess = "berte"
test = ""
yellow = ""

loop1 = 5
loop2 = 6
loop_n = 5

w_i = 0
g_i = 0
w_index = 0
g_index = 0 


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
print(yellow)