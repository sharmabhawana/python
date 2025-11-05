'''In the publishing house, there is a mischievous "Rogue Editor" who accidentally holds down keys too long, leaving behind consecutive duplicate characters in manuscripts. Your task is to clean the text by collapsing every group of consecutive duplicates into a single character, while keeping the original order of characters intact. All symbols, numbers, and letters must be preserved exactly as they appear (just without the duplicates).
Input Format
A single string.
Constraints
Preserve case (uppercase and lowercase are different). Preserve non-letters (digits, punctuation, etc.). 0 ≤ length ≤ 1000.
Output Format
The cleaned-up string with consecutive duplicates collapsed.
Sample Input 0
aaabbbcc
Sample Output 0
abc
Sample Input 1
Hellooo!!
Sample Output 1
Helo!'''
n= input() 
t=""
for i in range(len(n)):
    if i==0 or n[i]!= n[i-1]:
        t+=n[i]
print(t)
