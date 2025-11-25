'''File handling demo
'''
"""fp=open("backup.txt","w")
print(fp.name,fp.mode,fp.closed,fp.encoding,sep=" ")
fp.close()
print(fp.closed)"""
'''fp=open("backup.txt","w")
msg=input("Enter ur message:")
print(msg)
fp.write(msg)
fp.close()'''
'''fp=open("backup.txt","a")
msg=input("Enter ur message:")
print(msg)
fp.write("\n"+msg)
fp.close()'''
'''fp=open("output.txt","a")
num1,num2=map(int,input("enter two number sep by space:").split())
res=num1+num2
result=f"Sum of {num1} and {num2} ={res}\n"
print(result)
fp.write(result)
fp.close()'''
'''fp=open("output.txt","a")
lst=["noida,","deharadhun,","jammu,","roorke,","delhi"]
fp.writelines(lst)
fp.close()'''
'''
import os 
os.system("cls")
fp=open("backup.txt","r")
#text=fp.read()
print(fp.read())
fp.seek(0)#For cursor movement
print(fp.read())
fp.close()'''
'''import os 
os.system("cls")
fp=open("backup.txt","r")
#text=fp.read()
print(fp.read(10))
##print(fp.read())
fp.close()'''
'''import os 
os.system("cls")
fp=open("backup.txt","r")
for i in range(5):
    print(fp.readline(),end="")
fp.close()'''
'''import os 
os.system("cls")
fp=open("backup.txt","r")
lst=fp.readlines()
for line in lst:
    print(line,end="")
fp.close()'''
'''import os 
os.system("cls")
fp=open("backup.txt","r")
for line in fp.readlines()[::-1]:
    print(line,end="")
fp.close()
'''
import os 
os.system("cls")
fp=open("output.txt","r")
for line in fp.readlines():
    line=line.strip("\n")
    if line==line[::-1]:
        print(line," is palindrome")
    else:
        print(line," is not palindrome")
fp.close()