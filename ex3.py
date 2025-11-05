#Activity3:- Performing string slicing and basic operation on string object

st="Welcome to Python world"

#counting number of alphabets
import string
allalpha= string.ascii_letters
count=0
for char in st:
  if char in allalpha:
    count+=1
print(f"no of alphabets in string ={count}")


#extract character in a given range
startindex=int(input("enter start index:"))
endindex=int(input("enter end index:"))   #end index will be exclusive
newstr=st[startindex:endindex]
print(newstr)


#checking whether string is alpha numeric or not
if st.isalnum():
  print("String is alphanumeric")
else:
  print("String is not alphanumeric")