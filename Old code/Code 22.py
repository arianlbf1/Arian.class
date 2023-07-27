number = int(input("Please enter a 3 digit number:"))
num1 = number % 10
num2 = (number // 10) % 10
num3 = number // 100
num4 = num1 + num2 + num3
print(num4)