score=0
print ("Hello!")
print ("Today i am going to ask some questions, remember to not use capital letters.")
num1=input("Are you ready to play? (yes/no):")
if num1 == 'yes': 
    num2=int(input("What is my favorite number?"))
    if num2 == 7:
        print ("Correct, lets move on to the next one.")
        score=score+1
    else:
        print("Incorrect, I am disappointed in you.")
    num3=input("what is my favourite colour?")
    if num3 == 'blue':
        print("correct, that was an easy one.")
        score=score+1
    else:
        print("Incorrect, that was so easy, how the hell did you mess that up???")
    num4=input("What is my favourite sport?")
    if num4 == 'football':
        print ("Correct, I am so glad you didn’t call it soccer.")
        score=score+1
    elif num4 == 'soccer':
        print("Why would you call it soccer? Im reseting your score because of that.")
        score=0
    else:
        print ("you got it incorrect, but at least you didn’t say soccer.")
elif num1 == 'no':
    print ("Ok, have a great day.")
else:
    print ("ERROR (your answer was not yes/no.)")
mark=(score*100)/3
print("mark: ", mark)
print ("your score was", score)