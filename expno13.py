
'''import os
fname=input("Enter file name:")
f=open(fname,"w")#opening file in writting mode
msg=input("enter your message:")
f.write(msg)#writing message to file
f.close()#closing the file
print("Data written successfully in file...")
input("Press enter to continue...")
os.system('cls')
f=open(fname,"r")#opening file in reading mode
string=f.read()
res=sorted(set(string.split(" ")))
for word in res:
    print(word,end=" ")
f.close()'''
import os
fname=input("Enter file name:")
f=open(fname,"w+")#opening file in writting mode
msg=input("enter your message:")
f.write(msg)#writing message to file
print("Data written successfully in file...")
input("Press enter to continue...")
os.system('cls')
f.seek(0)
string=f.read()
res=sorted(set(string.split(" ")))
for word in res:
    print(word,end=" ")
f.close()