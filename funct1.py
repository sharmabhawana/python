#Pass by object references
'''1. Python supports call by value (Where the value is always an object reference,not the value of the object )
2. Hence many professionals terms it as Pass by object reference'''
'''lst=["MIET"]
def test(p):
    p.append("Jammu")
print(lst)
test(lst)
print(lst)'''
'''
lst=["MIET"]
def test(p):
    p.append("Jammu")
print(lst)
test(lst)
print(lst)lst="MIET"
def test(p):
    p=p+"Jammu"
print(lst)
test(lst)
print(lst)'''
'''lst=["MIET"]
def test(p):
    p=["Jammu"]
print(lst)
test(lst)
print(lst)'''
#Function(Local and global variables)
'''Scopes-> Local 
inclosing
global
built in
'''

'''Local variable
The variable defined within the function has a local scope and hence they are called local variables.
Local means they can be accessed within the function only.
They appear when the function is called and disappear when the function exists.
Global variable
'''
'''num=10
def test():
    num=100
    print(num)
test()
print(num)
num=100
def test():
    global num
    num+=100
    print(num)
test()
print(num)'''
#context switching
def fun2():
    z=30
    print("inside fun2")
def fun1():
    y=20
    print("inside fun1")
    fun2()
    print("end of fun1")
print("inside main")
fun1()  
print("end of main")