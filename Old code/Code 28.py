def power_code():
    num1=int(input("Please enter the first number:"))
    num2=int(input("Please enter the second number:"))
    num2=num2-1
    while not num2 == 0:
        num3=num1
        num1=num1*num3
        num2=num2-1
    print(num1)
    
def square_code():
    num4=int(input("Please enter the number you want to square:"))
    num4=num4*num4
    print(num4)
power_code()
square_code()