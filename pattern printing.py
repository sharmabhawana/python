"""for i in range(1,6):
    for j in range(i):
        print("* ",end="")
    print()
"""
"""for i in range(1,6):
    for j in range(i):
        print(i," ",end="")
    print()
"""
"""for i in range(1,6):
    for j in range(i):
        print(j+1," ",end="")
    print()
"""
"""for i in range(1,6):
    for j in range(i):
        if j%2==0:
            print("0"," ",end="")
        else:
            print("1"," ",end="")
    print()
"""
"""count=1
for i in range(1,6):
    for j in range(i):
        print(count," ",end="")
        count+=1
    print()
"""
count=65
for i in range(1,6):
    for j in range(i):
        print(chr(count)," ",end="")
        count+=1
    print()
