num1 = 1
num2 = 0
num3 = 0
even = 0
odd = 0

while num1 <= 10:
    num2 = int(input("Please enter 10 numbers"))
    num3 = num2%2
    if num3 == 0:
        print("Your number was even")
        even = even+num2
    else:
        print("Your number was odd")
        odd = odd+num2
    num1= num1+1
print(odd)
print(even)