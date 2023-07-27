import time
num1=int(input("please enter the amount of hours you want to count down:"))
num2=int(input("please enter the amount of minutes you want to count down: "))
timer=int(input("please enter the amount of seconds you want to count down: "))
if not num1==0:
    num1=num1*60
if not num2==0:
    timer=num2*60
while not timer==0:
    print(timer, "seconds left")
    time.sleep(1)
    timer=timer-1
print("Your time is up!")