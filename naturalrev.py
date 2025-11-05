#2.	Write a python program to print all natural numbers in reverse (from n to 1). - using while loop
num= int(input("Enter n: "))
i = num
while i >= 1:
    print(i, end=' ')
    i -= 1
