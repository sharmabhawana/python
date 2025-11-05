#6.	Write a python program to print multiplication table of any number.
num = int(input("Enter number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1