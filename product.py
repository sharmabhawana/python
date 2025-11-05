#10.Write a python program to calculate product of digits of a number.
num = int(input("Enter a number: "))
product = 1
if num == 0:
    product = 0
while num > 0:
    digit = num % 10
    product *= digit
    num //= 10
print("Product of digits:", product)