'''Long ago, during a secret war of codes, messengers used dots (.) and dashes (-) to send encrypted signals across great distances. Over time, those marks found their way into ordinary writings, but their meaning often caused confusion. To restore clarity, you must help the scribes translate every dot and dash into words.
However, there is a rule: if a dot belongs to a decimal number, it must remain untouched (since numbers like 3.14 or 12.5 are important and cannot be altered). But everywhere else, a dot must be replaced with (dot) and a dash must become (dash).
Your mission is to take a given message and transform it into its "Morse-less" form so that no one mistakes ordinary text for secret code.
Input Format
A single string (report).
Constraints
Case-sensitive (so 'A' and 'a' are different). 1 ≤ length ≤ 1000.
Output Format
The first non-repeating character, or -1 if none exist.
Sample Input 0
Wait... what?
Sample Output 0
Wait(dot)(dot)(dot) what?
Sample Input 1
3.14 is pi
Sample Output 1
3.14 is pi'''
m=input().strip()
r=[]
for i in range(len(m)):
    char=m[i]
    if char=='.':
        if i>0 and i<len(m)-1:
            if m[i-1].isdigit() and m[i+1].isdigit():
                r.append('.')
            else:
                r.append('(dot)')
        else:
            r.append('(dot)')
    elif char=='-':
        r.append('(dash)')
    else:
        r.append(char)
t=''.join(r)
print(t)