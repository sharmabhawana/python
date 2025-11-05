'''Ravi, a history student, keeps a personal diary where he writes down important words or phrases he learns every single day. Unfortunately, one day while shifting rooms, some of the pages of his diary got shuffled and were later entered into a computer in the form of a list of words. Now, Ravi’s professor, while reviewing his diary entries, suddenly asks him: “Can you tell me what was the k-th word you wrote down in your diary?” Since Ravi is a bit confused due to the shuffled pages, your job is to help him by writing a program that prints the k-th word from the given list of words. Remember, the indexing is 0-based (the first word is at index 0, the second at index 1, and so on).
Input Format
A list of words representing Ravi’s diary entries. An integer k, representing the position in the list (0-based).
Constraints
1 ≤ length of list ≤ 1000 Each word contains only alphabets (a–z or A–Z). 0 ≤ k < length of list Words can have a maximum length of 20 characters.
Output Format
Word at index k
Sample Input 0
["hello","world","python","rocks"], 2
Sample Output 0
python
Sample Input 1
["hackathon","contest","list"], 0
Sample Output 1
hackathon
Submissions: 31
Max Score: 5
Difficulty: Medium
Rate This Challenge:
More
1
​'''
n= input().strip()
l,k= n.rsplit(",", 1)
w=l.strip()[1:-1].replace('"', '').split(',')
s=int(k.strip())
print(w[s])