num1 = 0
num2 = 0
num3 = 0
num4 = 0
for i in range(10):
    num2=0
    num1=num1+1
    num4=num4+1
    print(num4, "Tables")
    for y in range(10):
        num2=num2+1
        num3=num2*num1
        print(num1, "*", num2, "=", num3)
