import time
num1=0
MAX=0
print("LCM machine loading...")
time.sleep(2)
x=int(input("please enter 2 numbers(X)"))
print("Loading...")
time.sleep(1)
y=int(input("please enter 2 numbers(Y)"))
print("Calculating bigger number...")
time.sleep(2)
if x<y:
    print("Y bigger")
    MAX=y
else:
    print("X bigger")
    MAX=x
print("Loading...")
time.sleep(1)
print("Your bigger number was", MAX)
print("Calculating LCM...")
time.sleep(3)
while num1==0:
    if MAX%y==0 and MAX%x==0:
        LCM=(MAX)
        break
    MAX=MAX+1
print("Your LCM was", LCM)