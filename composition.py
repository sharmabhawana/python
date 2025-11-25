class Address:
    def __init__(self,street,city,state):
        self.street=street
        self.city=city
        self.state=state
    def printAddress(self):
        print(f"""Street:{self.street} City:{self.city}
State:{self.state}""")
class Student:
    def __init__(self,rollno,name,address):
        self.rollno=rollno
        self.name=name
        self.address=address
    def printDetails(self):
        print(f"RollNo:{self.rollno} name:{self.name}")
        self.address.printAddress()
        
class Employee:
    def __init__(self,eid,name,address):
        self.eid=eid
        self.name=name
        self.address=address
    def printDetails(self):
        print(f"Eid:{self.eid} name:{self.name}")
        self.address.printAddress()
A=Address()
A.printAddress(10001,'noida','J&k')
s=Student()
s.printDetails(101,'james',A)



