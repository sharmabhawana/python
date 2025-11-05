''' Password Validator	
Check if a password:
Has at least one uppercase letter
Has one digit
Has one special character
Is 8-16 characters long
'''
import string
password=input("Enter your password: ")
upper = False
digit = False
special = False
special_characters = string.punctuation
if 8 <= len(password) <= 16:
    for char in password:
        upper |= char.isupper(); digit |= char.isdigit(); special |= char in special_characters
if upper and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")