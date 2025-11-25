#create a text file in python and ak the user to separate 3 lines and three input statements from the user.
'''fname=input("Enter Number of lines to write in file:")
f=open("MyFile.txt","w")
for i in range(int(fname)):
    line=input(f"Enter line {i+1}:")
    f.write(line+"\n")
    print(line)
f.close()'''
import os
fname=input("Enter file name:")
f=open(fname,"w+")#opening file in writting mode
msg=int(input("enter no of lines:"))
for i in range(msg):
    line=input(f"Enter line :") +"\n"
    f.write(line)#writing message to file
print("Data written successfully in file...")
input("Press enter to continue...")
os.system('cls')
f.seek(0)
print(f.read())
f.close()