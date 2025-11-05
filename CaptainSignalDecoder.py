'''On a distant voyage, the starship captain receives encrypted signals from allied ships. Each signal is divided into groups of letters, separated by the | symbol. The encryption rule is strange:
If a group's length is odd, the message has been shifted to the left by one character. To decode it, you must rotate it left once (move the first character to the end).
If a group's length is even, the message has been shifted to the right by one character. To decode it, you must rotate it right once (move the last character to the front).
Your mission is to reconstruct the entire decoded message by applying the rule to each group and then joining them back with |.
Input Format
single line (groups separated by |).
Constraints
groups non-empty.
Output Format
transformed line.
Sample Input 0
abc|de|fghi
Sample Output 0
bca|ed|ifgh
Sample Input 1
x|yz
Sample Output 1
x|zy'''
s=input()            
g=s.split('|')    
d=[]                   
for i in g:
    c=list(i)   
    if len(c)%2!=0:
        c.append(c.pop(0))
    else:                     
        c.insert(0, c.pop())
    d.append(''.join(c))
print('|'.join(d))   
        