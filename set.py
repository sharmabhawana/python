#st=set(['M','I'])
#print(st)
'''st={"James","James","king","Blake","King"}
print(st)'''
#print((st)[::-1]) it raise error because can't preserve order
#st=set()
#print(type(st))
'''st1=["red","blue"]
st2=["blue","green"]'''#True because in set order is not preserved
'''st=set()#adding elements to set
st.add(10)
print(st,id(st))
st.add(20)
print(st,id(st))
st.add(30)
print(st,id(st))
#Remove 
st.remove(20)
print(st,id(st))
st.remove(10)
print(st,id(st))
st.remove(30)
print(st,id(st))'''
'''st={12,12.3,12+5j,"hello",(10,20),"James"}#immutable
print(st)'''
fac={"c","cpp","java","php"}
st={"js","python","c","cpp"}
'''print("fac:",fac)
print("st:",st)'''
#newset=fac.union(st)
#fac.update(st)
#print("Union",newset)
#print("update",fac)
#newset=fac.intersection(st)
#print("Intersection",newset)
#fac.intersection_update(st)
#print("Intersection update",fac)
#newset=fac.difference(st)
#print("Difference",newset)
#newset=st.difference(fac)
#print("Difference",newset)
'''
newset=fac.symmetric_difference(st)
print("Difference",newset)'''
'''st1={"green","red","blue"}
st2={"green"}
print(st1.issubset(st2))
print(st1.issuperset(st2))'''
'''
st1={"red"}
st2={"green"}
print(st1.isdisjoint(st2))'''
fac={"c","cpp","java","php"}
st={"js","python","c","cpp"}
'''newset=fac|st
print(newset)'''
'''
newset=fac&st
print(fac|st)'''
'''
print(fac&st)
print(fac-st)
print(st-fac)
print(st^fac)
'''
#Frozen set is a immutable set
'''lst=frozenset(["James","neen","neena","blake","James"])
print(lst)'''
'''import math
n = int(input("Enter number:"))
print("Factorial:", math.factorial(n))
'''
'''s = "education"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowels:", count)'''
'''s=input("Enter string:")
count=0
for ch in s:
    if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        count+=1
        print("Vowel found:", ch)
    else:
        print("Consonant found:", ch)
print("Total Vowels:", count)
'''
'''n=int(input("Enter number:"))
t=int(input("Enter till:"))
for i in range(1,t+1):
    print(f"{n} x {i} = {n*i}")
'''
'''lst =input("Enter numbers separated by space:").split(" ")
print("Max:", max(lst))
print("Min:", min(lst))'''
'''lst =[23,45,12,67,34,89,22]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)'''
'''c=int(input("Enter Celsius:"))
f = (c * 9/5) + 32
print("Fahrenheit:", f)
f=int(input("Enter fahrenheit:"))
c=(f-32)*5/9
print("Celsius:", c)'''
'''n=int(input("Enter number:"))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''
'''lst =input("Enter numbers separated by space:").split(" ")
new_lst = list(set(lst))
print(new_lst)
'''
'''n=int(input("Enter number:"))
temp=n
sum=0
while n>0:
    d=n%10
    sum+=d**3
    n//=10
if sum==temp:
    print("Armstrong")
else:
    print("Not Armstrong")'''
