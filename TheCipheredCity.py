'''For each city name, move every uppercase letter to the front preserving relative order, then append lowercase letters preserving order.
Input Format
single string (one word; no spaces).
Constraints
letters only, length ≤ 100.
Output Format
transformed string.
Sample Input 0
NewYork
Sample Output 0
NYework
Sample Input 1
delhi
Sample Output 1
delhi'''
city=input().strip()
uppercase=""
lowercase=""
for i in city:
    if i.isupper():
        uppercase=uppercase+i
    else:
        lowercase=lowercase+i
print(uppercase+lowercase)