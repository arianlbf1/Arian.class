
scentence = input("Please write a scentence:")

words = [word.lower() for word in scentence.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)
