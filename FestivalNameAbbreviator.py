'''Create an abbreviation: take first letters of each word, uppercase them.
Input Format
a line with 2-10 words.
Constraints
words contain letters and single space only.
Output Format
abbreviation string.
Sample Input 0
independence day
Sample Output 0
ID
Sample Input 1
International Yoga Day
Sample Output 1
IYD'''
n=input().split(" ")
l=""
for i in n:
    l=l+i[0].upper()
print(l)