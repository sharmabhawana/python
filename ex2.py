
#Activity-8:-Python program that converts temperature to and from Celsius and Fahrenheit. The user can choose the direction of conversion. 


print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit =  (celsius * 9/5) + 32
    print(str(celsius)," C is equal to ",str(fahrenheit)," F")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(str(fahrenheit)," F is equal to ",str(celsius),"°C")

else:
    print("Invalid choice. Please enter 1 or 2.")