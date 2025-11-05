'''In a quiet library, a meticulous librarian was reviewing pages of an old manuscript. She had a peculiar habit: she wanted every page to contain all 26 letters of the English alphabet at least once. Pages that were missing letters made her frown because she believed a perfect page should have the full set of letters.
To help her, you are tasked with writing a program that will:
Take a line of text (which may include spaces, punctuation, or numbers).
Count how many unique letters of the English alphabet(a–z) are missing from that line.
Treat letters as case-insensitive (so 'A' and 'a' are considered the same).
This way, the librarian can quickly know if a page is complete or which letters she should add to make it perfect.
Input Format
a single line string (may include spaces, punctuation).
Constraints
treat only a–z; length ≤ 1000.
Output Format
integer — count of missing English letters (case-insensitive)
Sample Input 0
the quick brown fox jumps over the lazy dog
Sample Output 0
0
Sample Input 1
hello world!
Sample Output 1
19'''
n=input().lower()
l=set()
for ch in n:
    if 'a'<=ch<='z':
        l.add(ch)
m=26-len(l)
print(m)