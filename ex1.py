'''Activity -1:- To demonstrates type checking of various data types and the use of the following built-in functions:

abs(),len(),min(),round(),isalnum(),type()'''


# Define variables of different data types
integer_num = -25
float_num = 7.895
string_text = "Hello123"
list_data = [10, 20, 30, 5, 15]
mixed_string = "Welcome!"
alphanumeric_string = "Test123"

# 1. type(): Returns the type of a variable.
#Examples:
print("1. type() function:")
print("Type of integer_num:", type(integer_num))       
print("Type of float_num:", type(float_num))           
print("Type of string_text:", type(string_text))       
print("Type of list_data:", type(list_data))       
print()

# 2. abs(): Returns the absolute (non-negative) value of a number.
#Examples
print("2. abs() function:")
print("Absolute value of", integer_num, "is", abs(integer_num))  
print()

# 3. len(): Returns the number of items in an object (string, list, etc.)
#Examples
print("3. len() function:")
print("Length of string_text is", len(string_text))     
print("Length of list_data is", len(list_data))         
print()

# 4. min(): Returns the smallest item in an iterable or between arguments.
#Examples
print("4. min() function:")
print("Minimum in list_data is", min(list_data))        
print()

# 5. round(): Rounds a number to the nearest integer or specified decimal places.
#Examples
print("5. round() function:")
print("Rounded value of", float_num, "is", round(float_num))      
print("Rounded value to 2 decimals:", round(float_num, 2))         
print()

# 6. isalnum(): Returns True if all characters in the string are alphanumeric (letters or digits).
#Examples
print("6. isalnum() function:")
print("Is string_text alphanumeric?", string_text.isalnum())       
print("Is mixed_string alphanumeric?", mixed_string.isalnum())     
print("Is alphanumeric_string alphanumeric?", alphanumeric_string.isalnum())