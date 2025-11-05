'''Two spies exchange messages. If entire string is a palindrome (ignoring spaces/case), print PAL, else print the string with first and last characters swapped.
Input Format
single line S.
Constraints
1 ≤ len ≤ 200.
Output Format
either PAL or transformed string.
Sample Input 0
madam
Sample Output 0
PAL
Sample Input 1
step on no pets
Sample Output 1
PAL'''
S=input()
n=S.replace(" ", "").lower()
if n==n[::-1]:
    print("PAL")
else:
    if len(S)==1:
        print(S)
    else:
        print(S[-1]+S[1:-1]+S[0])
