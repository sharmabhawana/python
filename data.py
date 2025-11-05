database=[]
def createdatabase():
        count=int(input("Enter number of students:"))
        for i in range(count):
            sid=int(input("Enter Student ID:"))
            name=input("Enter Student name:")
            cgpa=float(input("Enter Student CGPA:"))
            branch=input("Enter Student Branch:")
            email=input("Enter Student Email:")
            record=(sid,name,cgpa,branch,email)
            database.append(record)
def printdb():
    print("Student Database".center(70,"-"))
    print(f"{'sid':<10}{'name':<15}{'cgpa':<10}{'branch':<15}{'email':<20}")
    print("".center(70,"-"))
    for record in database:
        print(f"{record[0]:<10}{record[1]:<15}{record[2]:<10}{record[3]:<15}{record[4]:<20}")
    print("".center(70,"-"))
createdatabase()
printdb()
print("Developed by ER.Bhawana Sharma")