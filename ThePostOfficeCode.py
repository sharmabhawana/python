'''In a bustling town, the postmaster had a unique way of encoding building names to make sure letters and parcels reached the correct destinations. His rule was simple but tricky:
For every word in the building name, if the word has an even number of letters, he would reverse the letters.
If the word has an odd number of letters, he would leave it unchanged.
Your task is to help the postmaster by writing a program that takes a sentence of building names and applies his encoding rule, so the delivery system remains flawless.
Input Format
A single line — a sentence (words separated by single spaces).
Constraints
length ≤ 200.
Output Format
Transformed sentence.
Sample Input 0
Main Street
Sample Output 0
niaM teertS
Sample Input 1
Central Park
Sample Output 1
Central kraP'''
n=input()
t=[]
for i in n.split(" "):
    if len(i) % 2 == 0:
        t.append(i[::-1])
    else:
        t.append(i)
res=" ".join(t)
print(res)