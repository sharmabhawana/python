#t=tuple(iter) For existing object into tuple.
#t=(1,2,3,4) For scratch or new tuple
#t=tuple("James")
#print(t,type(t))
'''t=('J', 'a', 'm', 'e', 's')
print(t,type(t))
t=10,20,30
print(t,type(t))
t=[10],[20],[30]
print(t,type(t))
a,b,c=t
print(f"a:{a} b:{b} c:{c}")
t=10,20,30,40,50
a,*b,c=t# * it contains 0 or more extra parameter in tuple.
print(t)
t=10,20
*a,b,c=t# * it contains 0 or more extra parameter in tuple.
print(t)
#swapping
num1,num2=int(input("Enter first number:")),int(input("Enter Second number:"))
print(f"Before swap num1:{num1} num2:{num2}")
num1,num2=num2,num1
print(f"After swap num1:{num1}  num2:{num2}")
#Fibonacci Series
num1,num2=0,1
for i in range(10):
    print(num1,end=" ")
    num1,num2=num2,num1+num2  
    num1=(10,)
#print(type(num1)) 
'''
#There are only two methods in tuple
'''t=(12,12.4,12+5j,True,"James",[10,20,30,40,50])
t[-1].append(1000)
print(t)
t=(10,20,30,40,50)
print(t.count(30))
print(t.index(40))
'''
#Dictionary
'''
name={"james":3000,"King":4000,"Blake":5000,"Neena":9000}
print(name["james"])'''
#d1={'r':'red','b':'blue'}
#d2={'b':'blue','r':'red'}
#print(d1==d2)
#Empty Dictionary
'''
d=dict()
d={}
print(d,id(d))
d['r']='red'
print(d,id(d))
d['b']='blue'                                
print(d,id(d))
d['b']='black'
print(d,id(d))
del(d['r'])
print(d,id(d))
d={"int":10,"str":"james","List":[10,20,30],"tuple":(10,)}'''

