st="welcome to the world of string"
'''st=st.upper()
print(st)
st=st.lower()
print(st)
st=st.capitalize()
print(st)
st=st.title()
print(st)
st=st.swapcase()
print(st)
'''
"""name="Bhawana"
age=19
print("my name is ",name,"and i am ",age,"year's old")
print("my name is "+name+" and i am "+str(age)+" year's old")
print("my name is %s and i am %d year's old"%(name,age))
print("my name is {} and i am {} year's old".format(name,age))
'''emp=[101,"james","james@gmail.com,10"]
print("eid: {} name: {} email: {} did: {}" .format(*emp))
'''
print(f"my name  is {name} and i am {age} year's old")"""
'''headings=["eid","name","email","salary","did"]
emp1=[101,"James","James@gmail.com",60000,10]
print("{:<5}{:<15}{:<20}{:<9}{:<4}".format(*headings))
print("-"*120)
print("{:<5}{:<15}{:<20}{:<9}{:<4}".format(*emp1))'''
'''st="15000$"
print(st.ljust(40,'-'))
print(st.center(40,'-'))
print(st.rjust(40,'-'))'''
'''st="PYTHON"
bst=st.encode(encoding="ascii",errors="strict")
print(bst)
bst=st.decode(encoding="ascii",errors="strict")
print(bst)'''
'''st="PYTH"+"\u229a"+"N"
bst=st.encode(encoding="ascii",errors="ignore")
print(bst)
bst=st.encode(encoding="ascii",errors="replace")
print(bst)
bst=st.encode(encoding="ascii",errors="namereplace")
print(bst)'''
'''pwd="bhawana@123"
import hashlib
encstr=hashlib.md5(pwd.encode())
print(encstr.hexdigest())'''
'''pwd="e09b79e2bc2715b3288d9e97e5a1b382"
import hashlib
password=input("enter ur password")
password=hashlib.md5(password.encode())
print(password.hexdigest())'''
'''st="mississippi"
print(st.count("s"))
print(st.count("s",4,8))
print(st.index("p"))
'''
'''st="python is high level language"
st1="aeiou"
st2="12345"
ttab=str.maketrans(st1,st2)
print(ttab)
res=st.translate(ttab)
print(st)
print(res)'''
'''st="python is high level language"
st1="aeiou"
st2="*****"
ttab=str.maketrans(st1,st2)
print(ttab)
res=st.translate(ttab)
print(st)
print(res)'''
'''st="python is high level language"
import string
st1=string.ascii_lowercase
st2=st1[::-1]
#print(st1,st2,sep="\n")
ttab=str.maketrans(st1,st2)
#print(ttab)
res=st.translate(ttab)
#print(st)
print(res)
print(res.translate(ttab))'''
#string to list convesrsion and list to string
'''st="noida,dehardhun,jammu,delhi,ghaziabad"
res=st.split(",")
#res=st.split(",",1)
print(res)
newstr="-".join(res)
print(newstr)'''
'''st="Mr james.,Mr king.,Mr Blake.,Mr Paul."
res=st.split(",")
print(res)
for i in res:
    print(i.lstrip("Mr"))'''
    #print(i.rstrip("."))
'''st="     malayalam"
#print(st.lstrip("m"))
#print(st.rstrip("m"))
#print(st.strip("ma"))
print(st.strip())'''
'''contactno=input("Enter ur number:")
if contactno.isdigit() and len(contactno)==10:
    print("Valid")
else:
    print("Invalid contact")
'''
#st="hello"
#print(st.islower())
#print(st.isupper())
'''st="hello"
print(st.isalpha())
'''
'''st="python is high level language"
res=st.replace("python","js")
print(res)
'''
'''a,b,c=map(int,input("Enter 3 numbers sep by space ").split())
print(a+b+c)'''
'''a=list(map(int,input("Enter  number sep by space ").split()))
print(a)'''
'''a=list(map(float,input("Enter 3 numbers sep by space ").split()))
print(a)'''
#print("hello".upper().count("L"))
st="abracadabara"
print(st[0]+st[1:].replace(st[0],"$")) 
#delete hello from the list
'''st=["Racecar","123@gmail.com","hello","Noon"]
st.remove("hello")
print(st)'''
'''st=input("Enter a string :")
if st==st[::-1]:
    print("Palindrome ")
else:
    print("Not Palindrome")'''
'''st=input("Enter a string:")

if st=="a" or st=="e" or st=="i" or st=="o" or st=="u" or st=="A" or st=="E" or st=="I" or st=="O" or st=="U":
    print("Vowels")
else:
    print("Consonant")'''