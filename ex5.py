stulist=[]
n=int(input("Enter number of students: "))
for i in range(n):
    d={}
    rno=int(input("Enter roll number: "))
    name=input("Enter name: ")
    branch=input("Enter branch: ")
    email=input("Enter email: ")
    d={"Roll No":rno,"Name":name,"Branch":branch,"Email":email}
    stulist.append(d)
for i in stulist:
    print(i)
num=int(input("Enter the number to  be searched: "))
found=0
for i in stulist:
    if i["Roll No"]==num:
        print("found:",i)
        print(i)
        found=1
        break
if found==0:
    print(" Not found")