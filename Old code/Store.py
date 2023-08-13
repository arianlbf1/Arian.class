i=0

shop = ['pencil', 'eraser', 'sharpener', 'pen', 'ruler']
item = input("What item do you want?")
for i in range (5):
    if item == shop[i]:
        print("We have your item, how many do you want?")
        amount = input()
        print("Successful purchase!")  