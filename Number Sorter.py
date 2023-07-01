list_length1 = int(input("How many numbers do you want to sort:"))
list_length = list_length1
unsorted_numbers = []
while not list_length1 == 0:
    list_number = int(input("Enter all the numbers that you want sorted:"))
    unsorted_numbers.append(list_number)
    list_length1 -= 1
sorted_numbers = []
even_numbers = []
unsorted_numbers = unsorted_numbers
i = 0
loop1 = 10
loop2 = list_length
loop3 = list_length

while not loop2 == 0:
    loop1 = 10
    smallest = unsorted_numbers[0]
    while not loop1 == 0:
        if i >= list_length:
            i = 0
        index = unsorted_numbers[i]
        if index < smallest:
            smallest = index
        elif index > smallest:
            smallest = smallest
        i += 1
        loop1 -= 1
    unsorted_numbers.remove(smallest)
    sorted_numbers.append(smallest)
    list_length -= 1
    loop2 -= 1
print(sorted_numbers)
sorted_numbers1 = sorted_numbers
i = 0

while not loop3 == 0:
    even_odd = sorted_numbers[i]
    if even_odd % 2 == 0:
        sorted_numbers.remove(even_odd)
        even_numbers.append(even_odd)
    else:
        sorted_numbers.remove(even_odd)
    loop3 -= 1
print(even_numbers)