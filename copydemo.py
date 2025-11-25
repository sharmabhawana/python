"""File copy demo"""
'''fpr=open("backup.txt","r")
fpw=open("copy.txt","w")
for line in fpr.readlines():
    fpw.write(line)
fpr.close()
fpw.close()

print("File copied Successfully....")'''

fpr=open("C:Users\BHAWANA SHARMA\OneDrive\Pictures\BST 2.png","rb")
fpw=open("copy.png","w")
for line in fpr.readlines():
    fpw.write(line)
fpr.close()
fpw.close()