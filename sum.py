#9.	Write a python program to find sum of first and last digit of a number.
num = int(input("Enter a number: "))
first_digit = num       
last_digit = num % 10
while first_digit >= 10:    
    first_digit //= 10
print("Sum of first and last digit:", first_digit + last_digit) 
