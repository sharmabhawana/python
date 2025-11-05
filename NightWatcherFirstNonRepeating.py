'''Every night, the town’s Watcher writes down strange noises in his report scroll as a sequence of characters. Most noises are repeated again and again, but sometimes a sound is unique — appearing only once in the whole report. The Watcher must quickly identify the first such unique sound. If no sound is unique, he records -1.
Input Format
A single string (report).
Constraints
Case-sensitive (so 'A' and 'a' are different). 1 ≤ length ≤ 1000.
Output Format
The first non-repeating character, or -1 if none exist.
Sample Input 0
swiss
Sample Output 0
w
Sample Input 1
aabb
Sample Output 1
-1'''
s=input().strip()
unique=[]
for ch in s:
    if s.count(ch)==1:
        unique.append(ch)
if unique:
    print(unique[0])
else:
    print(-1)