forest_A={"Tiger","Elephant","Deer","Monkey","Peacock"}
forest_B={"Deer","Monkey","Bear","Leopard","Fox"}
'''forest_A.add("Wolf")
forest_B.add("Wolf")
print("Forest A:",forest_A)
print("Forest B:",forest_B)
forest_A.remove("Elephant")
print("Forest A:",forest_A)
forest_B.discard("Tiger")
print("Forest B:",forest_B)
forest_A.discard("Panda")
print("Forest A:",forest_A)
#forest_A.remove("Panda")
newset=forest_A.union(forest_B)
print("Union:",newset)
newset=forest_B.symmetric_difference(forest_A)
print("only in b:",newset)
newset=forest_A.symmetric_difference(forest_B)
print("only in a:",newset)
newset=forest_A.intersection(forest_B)
print("Common in both:",newset)
# set of all unique species from both forest
newset=forest_A.union(forest_B)
print("All unique species:",newset)'''
'''a=["james","bond","neena","blake","james"]
for i,j in enumerate(a):
    if i==2:
        print(j)
    #print(i,j)'''
s={"Tiger","Elephant","Dear"}
print(s.issubset(forest_A))
print(forest_A.issuperset(s))
print(forest_B.isdisjoint(s))
print(forest_A.isdisjoint(forest_B))
#find if "peacock is present in forest B"
print("Peacock" in forest_B)
print("Bear" in forest_A)
#copyof forest A
copyforestA=forest_A.copy()
print("Copy of forest A:",copyforestA)
#clear forest A data and remain it unchanged
#forest_A.clear()
#print("Forest A:",forest_A)