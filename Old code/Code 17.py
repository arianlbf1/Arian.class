for i in range(50):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort(reverse=False)
print("Sorted numbers:", numbers)