'''Detective Arin was known for solving mysteries not by chasing suspects, but by spotting hidden patterns in evidence. One evening, he received a coded message and a long report. The challenge was simple but tricky: he needed to determine whether the secret pattern string (P) appeared inside the longer text (T).
Since criminals often try to confuse investigators with different letter cases, the detective decided to ignore whether letters were uppercase or lowercase. What mattered was the sequence of characters.
If the pattern was present, Arin would report the 0-based index of its first occurrence. If the pattern was nowhere to be found, he would simply write -1. This simple technique often uncovered the first clue in a long chain of evidence.
Now, you must step into the detective’s shoes and identify where the pattern lies—if it does at all.
Input Format
two lines — P then T.
Constraints
lengths ≤ 1000.
Output Format
integer index or -1.
Sample Input 0
abc
xxAbCyy
Sample Output 0
2
Sample Input 1
Hello
hey
Sample Output 1
-1'''
n=input().strip()
t=input().strip()
p=n.lower()
T=t.lower()
i=T.find(p)
print(i)