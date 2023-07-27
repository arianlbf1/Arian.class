import random
num1=0
choice=input("Would you like to role the dice:")
if choice=="yes":
    while num1==0:
        dice=random.randint(1, 6)
        print(dice)
        again=input("Would you like to go again:")
        if again=="yes":
            print("Alright.")
        elif again=="no":
            print("Alright, have a nice day!")
            num1=num1+1
            break
        else:
            print("ERROR, your answer has to be yes or no.")
            num1=num1+1
            break
elif choice=="no":
    print("Alright, have a nice day!")
else:
    print("ERROR, your answer has to be yes or no.")