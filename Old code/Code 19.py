num1 = int(input("Please enter a number:"))
num2 = 0
while num1 != 0:
    digit = num1 % 10
    num2 = num2 * 10 + digit
    num1 //= 10
print("Reversed Number:" + str(num2))