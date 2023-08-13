primen = 0
primet = 0
num1 = 1
num2 = 1
is_prime = True
while num1 < 100:
    num1 = num1 + 1
    is_prime = True
    num2 = 2
    while num2 < num1:
        if num1 % num2 == 0:
            is_prime = False
            break
        num2 = num2 + 1
    if is_prime:
        primen = primen+ 1
        primet = primet + num1
        print(num1)
print("the amount of numbers that were prime:", primen)
print("the total of numbers that were prime:", primet)