'''Chef sorts characters of each ingredient name alphabetically, but keeps ingredient order.
Input Format
single line with ingredients separated by commas (,). Trim spaces.
Constraints
each ingredient length ≤ 50, n ≤ 20.
Output Format
comma-separated transformed ingredients.
Sample Input 0
salt,pepper
Sample Output 0
alst,eepppr
Sample Input 1
onion,tomato,garlic
Sample Output 1
innoo,amoott,acgilr'''
t=input()
n=[]
for i in t.split(","):
    i=i.strip()
    sorted_item="".join(sorted(i))
    n.append(sorted_item)
print(",".join(n))