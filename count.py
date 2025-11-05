#7.	Write a python program to count number of digits in a number.
num = int(input("Enter a number: "))
count = 0
if num == 0:
    count = 1
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)