shopping = ["Apple", "Banana", "PC", "Cable", "Mcdonalds", "Iphone", "Ipad", "Watch"]
char1 = input("do you want to view your shopping list:")
char1 = char1.lower

if char1 == "yes":
    for letter in enumerate(shopping):
        print(letter)
elif char1 == "no":
    print("Thats sad")
else:
    print("ERROR")