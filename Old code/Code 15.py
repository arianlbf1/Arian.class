num1=int(input("Please enter three numbers:"))
num2=int(input())
num3=int(input())


if num1>num2:
    if num1>num3:
        num4=num1
    else:
        num5=num1
elif num1>num3:
    if num1>num2:
        num4=num1
    else:
        num5=num1
else:
    num6=num1

if num2>num1:
    if num2>num3:
        num4=num2
    else:
        num5=num2
elif num2>num3:
    if num2>num1:
        num5=num2
    else:
        num5=num2
else:
    num6=num2
    
if num3>num1:
    if num3>num2:
        num4=num3
    else:
        num5=num3
elif num3>num2:
    if num3>num1:
        num4=num3
    else:
        num5=num3
else:
    num6=num3
    
print(num4, num5, num6)
