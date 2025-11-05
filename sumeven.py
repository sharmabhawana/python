#5.	Write a python program to find sum of all even numbers between 1 to n.
n = int(input("Enter n: "))
sum = 0
for i in range(2, n+1, 2):
    sum += i
print("Sum of even numbers =", sum)