'''lst=["James","Neena","blake","neena","anna"]
print(f"before reverse {lst}")
#lst.reverse()
result=list(reversed(lst))
print(f"after reverse {result}")
print(f"after reverse {lst}")'''  

'''lst1=[10,[100]]
lst2=lst1.copy()
print(lst1,lst2)
lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)'''
import copy
lst1=[10,[100]]
#lst1=lst2 #interning
lst2=copy.deepcopy(lst1)#deep copy
print(lst1,lst2)
lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)