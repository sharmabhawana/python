"""lst=[12,12.5,12+5j,"James",True,[10,20,30],sum,len]
for i in lst:
    print(i,type(i))
print(lst[-2]([1,2,3,4,6]))
print(lst[-1]("James"))"""
'''lst=[]
print(lst,id(lst))
lst.append(10)
print(lst,id(lst))
lst.append(20)
print(lst,id(lst))
lst.append(30)
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))
'''
'''lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    for element in cl:
        if (element%2==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    for element in cl:
        print(element**2,end=" ")
    print()'''
'''lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j]=lst[i][j]**2
print(lst)'''
'''lst=[[1,2,3],4,5,6,[7,8,9]]
print(lst)
for i in lst:
    if type(i)==list:
        for j in i:
            print(j**2,end=" ")
        else:
            print(i**2,end=" ")'''
'''lst=[]
n=int(input("no of objects:"))
for i in range(n):
    lst.append(int(input("enter the num ")))
print(lst)'''
'''lst=[]
n=eval(input("no of objects:"))
for i in range(n):
    lst.append(eval(input("enter the no of object ")))
print(lst)'''
'''lst=list()
lst.append("James")
lst.append("King")
lst.append("Neena")
print(lst)
lst.insert(1,"paul")
print(lst)
lst.insert(1,"paul")
print(lst)
print(lst.count("paul"))
print(lst.index("paul",2,7))'''
'''lst1=["red","green","violet"]
lst2=["violet","cyan"]
lst1.extend(lst2)
#for i in lst2:
# lst1.append(i) 
print(lst1)'''

'''lst=list(range(2,11,2))
print(lst)
res=lst.pop(1)
print(f"popped element is {res}")
print(lst)
lst=["James","Neena","blake","neena","anna"]
lst.remove("neena")
print(lst)
del(lst[0])
print(lst)
lst.clear()
print(lst)'''
'''lst=["James","Neena","blake","neena","anna"]
print(f"before sort {lst}")
lst.sort()
print(f"after sort {lst}")'''
'''lst=["James","Neena","blake","neena","anna"]
print(f"before sort {lst}")
lst.sort(reverse=True)
print(f"after sort {lst}")'''
'''lst=["James","Neena","blake","neena","anna"]
print(f"before sort {lst}")
res=lst.sort(reverse=True)
print(f"after sort {lst}")
print(f"after sort {res}")'''
'''a=1e6
print(type(a))'''
'''print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
'''
a='123'
print(a.isdecimal())