"""Exception An exception is an event that occurs during execution of a program that disrupts the normal flow of program instruction.When this event occurs,Python generates an exception that can be handled which avoids your program to crash.
Exception are convenient in many ways for handling errors and special conditions in program.When u think that u have a code which can produce an error then u can use exception handling
You can raise an exception in ur own program by using the raise exception statement.
Raising an exception breaks current code execution and returns the exception back until it is handled."""
def div():
    print("Start of div function")
    
    try:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        res=num1//num2
        print(f"Result is {res}")
    except (ZeroDivisionError,ValueError) as ob:
        print(ob)
    except Exception as ob:
        print("Print class exception handler",ob)
    print("End of div function")
'''def test():
    print("Inside test function")
    div()
    print("End of test")'''
#def main():
print("Inside main function")
    #test()
div()
print("End of main")
#main()
"""Exception/Error handler
The runtime sysem searches the call stack for a method/function that contains a block of code that can handle exception.This  block of code is knowna s Exception handler.
The search begins with the method/function in which the exception occurred and produces through the call stack in the reverse order in which the methods/functions were called
When an appropriate handler is found,the runtime system passes the exception object to the handler.
An exception handler is considered appropriate if the type of the exception object thrown matches the type that can be handled by the handler.
Where exception may occurs
Hardware/os level
Arithmetic exception ;divide by 0,under,overflow
Memory access violations,stack over/underflow 
Language level
Bounds Violation: illegal issues
Value Error:invalid literal,improper casts
Program level
user defined exception
Keyword hadling keywords
They are five important keywords:
1)Try:Write the risky code here(code that may cause an exception).
2)except:Handles the exception.
3)else:Runs only when no exception occurs.
4)finally:Run always(important for cleanup).
5)raise:Used to manually raise an exception(used in custom exception)."""