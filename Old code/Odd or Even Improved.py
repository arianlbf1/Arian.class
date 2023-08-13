num0=0
num1=int(input("Please enter 10 numbers:"))
num2=int(input("Please enter 10 numbers:"))
num3=int(input("Please enter 10 numbers:"))
num4=int(input("Please enter 10 numbers:"))
num5=int(input("Please enter 10 numbers:"))
num6=int(input("Please enter 10 numbers:"))
num7=int(input("Please enter 10 numbers:"))
num8=int(input("Please enter 10 numbers:"))
num9=int(input("Please enter 10 numbers:"))
num10=int(input("Please enter 10 numbers:"))

odd_amount=0
odd_total=0
even_amount=0
even_total=0

number = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

for i in range(10):
    num0=number[i]%2
    if num0==1:
        odd_amount=odd_amount+1
        odd_total=odd_total+number[i]
    else:
        even_amount=even_amount+1
        even_total=even_total+number[i]
print("The amount of odd numbers were:", odd_amount)
print("The amount of odd numbers were", odd_total)
print("The amount of even numbers were:", even_amount)
print("The total of even numbers were:", even_total)