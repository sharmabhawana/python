"""empfp=open("emp.txt","r")
did=input("Enter did:")
for record in empfp.readlines():
    if did==record.split(",")[-1].rstrip("\n"):
        print(record,end="")
empfp.close()"""
'''empfp=open("emp.txt","r")
comm=input("Enter commission:")
for record in empfp.readlines():
    if record.split(",")[-3]!='Null':
        print(record,end="")
empfp.close()'''
#function for min and max salary
import os
empfp=open("emp.txt","r")
def salary():
    max=int(input("Enter max salary:"))
    min=int(input("Enter min salary:"))
    for i in  empfp.readlines():
        if min<=i.split(",")[-4]<=max:
            print(i,end=",")
salary()
empfp.close()


