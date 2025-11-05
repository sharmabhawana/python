"""Fun2 demo
Dev by BS"""#doc string
'''def add(num1:int,num2:int)->int:
    """add and return and
    #return an integer"""#block level string
    #return num1+num2#return sum its calling env #inline
print(help(add))'''

'''def add( *vararg):
    #var arg demo
    print(f"Sum of nums={sum(vararg)}")
add()
add(1)
add(1,2)
add(1,2,3)
add(1,2,3,4)'''
'''def add(**keyvararg):
    print("Sum of elements=",sum(keyvararg.values()))
    print(keyvararg)
add(a=10,b=20,c=30,d=40)

def testpara(a,b,*c,d=10,e=20,**f):
    print(f""" 
          a={a}
          b={b}
          c={c}
          d={d}
          e={e}
          f={f}""")
testpara(10,20,30,40,50,x=100,y=200,z=300,d=1000,e=2000)'''
'''def greet():
    return "hello world"
#res=greet#without this () it's give address of object
res=greet
print(res())
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    inner()
outer()'''
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    return inner
i=outer()
i()