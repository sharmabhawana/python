"""seek Demo"""
"""
fp=open("bkp.txt","rb")
'''print("Current file position:",fp.tell())
fp.read()
print("Current file position after reading 1st line:",fp.tell())'''
fp.seek(17,0)
print(fp.read(5).decode())
fp.seek(-10,1)
print(fp.read(4).decode())
fp.seek(7,1)
print(fp.read(8).decode())
fp.seek(-6,2)
print(fp.read(6).decode())
fp.close()"""
'''with open("bkp.txt","rb")as fp:
     fp.seek(17,0)
     print(fp.read(5).decode())
     fp.seek(-10,1)
     print(fp.read(4).decode())
     fp.seek(7,1)
     print(fp.read(8).decode())
     fp.seek(-6,2)
     print(fp.read(6).decode())
print(fp.closed)'''
'''Python pickle package
Pickle is used to serialize and deserialize a python object any object on python can be pickled so that it can be saved on disk.
Pickle first serialize the object and then converts the object into a character stream so that this character stream contain all the information neceaasry to reconstruct(deserialize )
the object data to the file.
Use pickle,dump(object,file) function to store the object data to the file
Use pickle,load(file) to retrieve pickled data.'''
import pickle
class Employee:
    def __init__(self,eid,name,sal,desig):
        self.eid=eid
        self.name=name
        self.sal=sal
        self.desig=desig
    def __str__(self):
        return(f"""Employee Details:
Eid:{self.eid}
Name:{self.name}
Sale:{self.sal}
Designation:{self.desig}""")
#print("enter eid name sal and designation ")
if __name__=="__main__":
    eid=int(input("Enter eid:"))
    name=input("Enter name:")
    sal=float(input("Enter sal:"))
    desig=input("Enter designation:")
    empobj=Employee(eid,name,sal,desig)
    
    fp=open("bkp.txt","wb")
    pickle.dump(empobj,fp)
    fp.close()
