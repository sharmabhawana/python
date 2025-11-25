import pickle
from seekdemo import Employee
fp=open("bkp.txt","rb")
obj=pickle.load(fp)
print(obj)
fp.close()