#WAP to create a simple calculator using match case and function for operation.
'''a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
match operator:
    case '+':
        result = a + b
        print("Result:", result)
    case '-':
        result = a - b
        print("Result:", result)
    case '*':
        result = a * b
        print("Result:", result)
    case '/':
        if b != 0:
            result = a / b
            print("Result:", result)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")'''
'''Write a python program that accepts the length of three sides of a triangle as inputs. The program should 
indicate whether or not the triangle is a right-angled triangle. (Use Pythagorean theorem) Also find out its 
area using Heron’s formula. '''
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))    
c = float(input("Enter length of side c: "))
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("The triangle is a right-angled triangle.")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("The area of the triangle is:", area)
else:
    print("The triangle is not a right-angled triangle.")
    