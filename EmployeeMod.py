from DepartmentMod import Department
from AddressMod import Address
class Employee:
    def __init__(self,eid,name,dept):
        self.eid=eid
        self.name=name
        self.dept=dept

    def __str__(self):
        return f"""EID: {self.eid}  Name: {self.name} {self.department}"""
class RegEmp(Employee):
    def __init__(self,eid,name,basic,hra,dept):
        super().__init__(eid,name,dept)
        self.basic=basic
        self.hra=hra
        self.salary=self.basic+self.hra

    def __str__(self):
        return f"{self.eid} {self.name} Salary: {self.salary} {self.dept}"
class DWEmp(Employee):
    def __init__(self,eid,name,dw,nod,dept):
        super().__init__(eid,name,dept)
        self.dw=dw
        self.nod=nod
        self.salary=self.dw*self.nod

    def __str__(self):
        return f"{self.eid} {self.name} Salary: {self.salary} {self.dept}"
reg=RegEmp(101,'james',40000,12000,Department(10, "IT",Address("street no-7", "noida", "up","343434")))
print(reg)
dwemp=DWEmp(102,'neena',800,22,Department(20, "HR",Address("street no-9", "delhi", "dl","343434")))
print(dwemp)