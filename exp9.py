import os
class Department:
    def __init__(self,did,name,location):
        self.did=did
        self.name=name
        self.location=location
    def __str__(self):
        return(f"""Department Details:  
Did:{self.did}
Name:{self.name}
Location:{self.location}""")
class Employee:
    def __init__(self,eid,name,department):
        self.eid=eid
        self.name=name
        self.department=department
class DailyWageEmp(Employee):
    def __init__(self,eid,name,dw,nod,dapartment):
        super().__init__(eid,name,dapartment)
        self.dw=dw
        self.nod=nod
        self.salary=self.dw*self.nod
        self.etype="Daily Wage"
    def updateSalary(self,newsal):
        self.dw=newsal
        self.salary=self.dw*self.nod
    def __str__(self):
        return(f"""{self.eid} {self.name} {self.salary} {self.etype} {self.department}""")
class RegularEmp(Employee):
    def __init__(self,eid,name,hra,basic,dapartment):
        super().__init__(eid,name,dapartment)
        self.hra=hra
        self.basic=basic
        self.salary=self.hra+self.basic
        self.etype="Regular"
    def updateSalary(self,newsal):
        self.basic=newsal
        self.salary=self.hra+self.basic
    def __str__(self):
        return(f"""{self.eid} {self.name} {self.salary} {self.etype} {self.department}""")
db=[]
while(True):
    os.system('cls')
    choice=int(input('''Main Menu
                     1.Insert Employee
                     2.Update Salary
                     3.Delete Employee
                     4. Search Employee
                     5.Show all Employee
                     6.Show all departments
                     7.Exit
                     Enter your choice:'''))
    if(choice==1):
        emp=None
        ch=int(input("1.Regular Employee 2.Daily Wage Employee"))
        eid=int(input("Enter Eid:"))
        name=input("Enter name:")
        did=int(input("Enter did:"))
        dname=input("Enter Dname:")
        loc=input("Enter location:")
        if ch==1:
            basic=int(input("Enter basic:"))
            hra=int(input("Enter HRA:"))
            emp=RegularEmp(eid,name,hra,basic,Department(did,name,loc))
        elif ch==2:
            dw=int(input("Enter daily wage:"))
            nod=int(input("Enter no of days:"))
            emp=DailyWageEmp(eid,name,dw,nod,Department(did,name,loc))
        db.append(emp)
        input("Press any key to continue...")
    elif(choice==2):
        eid=int(input("Enter eid :"))
        amt=int(input("Enter updated amount:"))
        for i in range (len(db)):
            if db[i].eid==eid:
                db[i].updateSalary(amt)
        input("Press any key to continue...")
    elif(choice==3):
        eid=int(input("Enter eid:"))
        for i in range (len(db)):
            if db[i].eid==eid:
                del(db[i])
                break
        input("Press any key to continue...")
    elif(choice==4):
        eid=int(input("Enter eid:"))
        for i in range (len(db)):
            if db[i].eid==eid:
                print(db[i])
                break
        input("Press any key to continue...")
    elif(choice==5):
        for i in db:
            print(i)
        input("Press any key to continue...")
    elif(choice==6):
        for i in db:
            print(i.department)
        input("Press any key to continue...")
    elif(choice==7):
        break
    else:
        print("Invalid choice")
        input("Press any key to continue...")
