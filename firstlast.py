#8.	Write a python program to find first and last digit of a number.
num = int(input("Enter a number: "))
first_digit = num
last_digit = num % 10
while first_digit >= 10:
    first_digit //= 10
print("First digit:", first_digit)
print("Last digit:", last_digit)