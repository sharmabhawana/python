lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def printlist(lst):
    for i in lst:
        print(i)
def reverse(lst,rno):
    for i in range(1,len(lst)+1):
        if i==rno:
            lst[i-1]=lst[i-1][::-1]
printlist(lst)
reverse(lst,int(input("Enter the valid row position:")))
printlist(lst)
print("Developed by ER.]Bhawana Sharma")