num1=0
num2=0
no_study=0
yes_study=0
average=0
while num1<15:
    num2=int(input("Please enter your scores (Between 0-20)"))
    if num2<15:
        print("You need to work on this topic more")
        yes_study=yes_study+1
        average=average+num2
        num1=num1+1
    elif num2>14 and num2<21:
        print("You do not need to study for this topic")
        no_study=no_study+1
        average=average+num2
        num1=num1+1
    elif num2>20:
        print("ERROR, your number did not meet the number range")
average=average/15
print("You need to study",yes_study,"topics")
print("You dont need to study",no_study,"topics")
print("The average number of your score was",average)