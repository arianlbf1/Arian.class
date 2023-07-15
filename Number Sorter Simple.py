list_length1 = int(input("How many numbers do you want to sort:"))
list_length = list_length1
unsorted_numbers = []
while not list_length1 == 0:
    list_number = int(input("Enter all the numbers that you want sorted:"))
    unsorted_numbers.append(list_number)
    list_length1 -= 1
sorted_numbers = []
even_numbers = []
i = 0
loop = list_length

while not loop == 0:
    smallest = min(unsorted_numbers)
    sorted_numbers.append(smallest)
    unsorted_numbers.remove(smallest)
    loop -= 1
print(sorted_numbers) 

loop = list_length

while not loop == 0:
    even_odd = sorted_numbers[i]
    if even_odd % 2 == 0:
        sorted_numbers.remove(even_odd)
        even_numbers.append(even_odd)
    else:
        sorted_numbers.remove(even_odd)
    loop-= 1
print(even_numbers)