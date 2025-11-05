import os

#Specify the directory you want to list
directory_path = ''
#list  all files and directories in the specified path.
contents = os.listdir(directory_path)

#List all files and directories in the specified directory
for item in contents:
    print(item)
