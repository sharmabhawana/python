#form a new list and print length of each string
'''lst=["Bhawana","Anjali","Pooja","Riya","Divya"]
lst1=[]
for i in lst:
    lst1.append(i)
    print(f"{i}:{len(i)}")
'''
#form a list and print length of each string and append length of string if<5
lst=["Bhawana","Anjali","Pooja","Riya","Divya","Anna","Eve","Tom"]
for i in lst[:]:
    if len(i)<5:
        lst.append(i)
print(lst)
