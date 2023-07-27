# Program to sort alphabetically the words form a string provided by the user

scentence = input("Please write a scentence:")

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words(word.lower() makes all the letters lowercase)
words = [word.lower() for word in scentence.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
