#4.	Write a python program to find sum of all natural numbers between 1 to n.
n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum =", sum)