#WAP to perform searching activity using linear and binary search using list of list as a user input.
'''lst=input("Enter the no of elements:").split(",")
for i in range (lst):
    lst.append(int(input("Enter the elements:")))
lst.sort()
print(lst)'''
num = list(map(int, input("Enter n numbers separated by space: ").split(" ")))
search = int(input("Enter number to search: "))
for i in range(len(num)):
    if num[i] == search:
        print(f"Linear Search: Found at index {i}")
        break
else:
    print("Linear Search: Not found")
# Binary Search (list must be sorted)
num.sort()
left = 0
right = len(num) - 1

while left <= right:
    mid = (left + right) // 2
    if num[mid] == search:
        print(f"Binary Search: Found at index {mid}")
        break
    elif num[mid] < search:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Binary Search: Not found")

