num = int(input("How many numbers?"))
a = 0
b = 1
c = 0
print (a)
print (b)
for i in range (2, num):
    c = a + b
    a = b
    b = c
    print (c)