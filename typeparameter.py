#Type of parameter
'''Parameter->Parameter is a variable in a function definition.
1. Mandatory parameter
2.Optional parameter
3.Keyword parameter
4.Vararg/Arbitary parameter *
5.Keyword vararg parameter **
'''
#1) Required positional/Manadatory argument
'''def printname(fname:str)->None:#hinting
    print(f"fname:{fname}")
printname(100)'''
#optional/Default parameter
'''def printname(fname,lname="na"):#hinting
    print(f"fname:{fname} lname:{lname}")
printname("james","bond")'''
'''def add(a,b):
    return a+b
def add(a,b,c=0):
    return a+b+c
def add(a,b,c=0,d=0):
    return a+b+c+d
print(add(10,20))'''
#keyword argument
'''def printname(fname,mname="na",lname="na"):#hinting
    print(f"fname:{fname} mname:{mname} lname:{lname} ")
printname(mname="k",lname="bond",fname="james")'''
