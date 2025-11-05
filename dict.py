#update
d1={"r":"red"}
d2={"g":"green"}
d={}
for i in d1,d2:
    d.update(i)
print(d)
#setdefault
d={}
d.setdefault("g","grey")
print(d)
d.setdefault("b","black")
print(d)
'''#d.clear()
#print(d)
print(d.popitem())
#print(d)
#d.popitem()#removes and returns an arbitrary (key, value) pair from the dictionary.
'''
'''d.pop("g")
print(d)
'''
d={'r': 'red', 'g': 'green', 'b': 'black'}
#d2=dict.fromkeys(d,0)
#print(d2)
'''for i in d:
    print(i,d[i])
print(d.keys())
print(d.values())
print(d.items())'''
'''for i in d.items():
    print(i,type(i))'''
'''for i in d.items():
    print(i[0],i[1])'''
'''for j in d.items():
        print(i,j)'''
'''print(d.get("z"))
print("Important code")'''