'''A teacher writes a string of uppercase letters representing candy types; students pick candies in pairs — find how many pairs (same letter) can be formed.
Input Format
single string (uppercase letters).
Constraints
0 ≤ length ≤ 1000.
Output Format
integer — total pairs.
Sample Input 0
AABBCC
Sample Output 0
3
Sample Input 1
AAAA
Sample Output 1
2'''
s=input().strip().upper()
n=[]
for ch in s:
    if ch not in n:
        n.append(ch)
pairs = 0
for ch in n:
    pairs += s.count(ch) // 2
print(pairs)
