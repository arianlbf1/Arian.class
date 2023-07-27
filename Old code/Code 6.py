num1=1
factor=0
y=1
x=int(input("Please enter a number"))
print("The factors for", x,"are,")
while num1==1:
    if x % y == 0:
        factor=y
        print(factor)
        factor=0
    y=y+1