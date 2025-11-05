#Function is a set of instructions that is used to perform a single related operation
'''Function are:
Organized
Reusable
Modularized
Python has many built in functions like print(), input(),int(),len().Etc but u can also create your own functions.
These functions are called user defined functions
Standard Library
Standard Library is a collection of tools that come in python.The standard Library includes the following: 
Built-in Functions
Modules
Packages'''#Package are the folders or may contain multiple modules is a collection of modules
#Module is a file containing python code
#Creating a function
'''
Syntax
def <function_name>(parameter1, parameter2, ...parameterN):
    statement1
    statement2
    return [expression]
    For example
    def myFunc(st):
        print(st)
        return st #End of the Function'''
#if there is no return in the function the it returns None by default
'''def sum():
    i,j=map(int,input("Enter two numbers:").split(" "))
    print("Sum is:",i+j)
sum()'''
'''def add():
    i=list(map(int,input("Enter two numbers:").split(" ")))
    print(sum(i))
add()'''
l,n,s=eval(input())
print(l,n,s,sep="\n")