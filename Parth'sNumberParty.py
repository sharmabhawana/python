'''Parth is organizing a small math challenge for his friends at a weekend party. As a fun twist, he gives them a simple task: "I'll give you n numbers. You have to keep a secret score: Add all the even numbers to your Even Score Add all the odd numbers to your Odd Score" Parth gives n numbers, and your job is to help his friends calculate both scores correctly.
Write a program that reads n numbers (one per line), and calculates:
The sum of all even numbers
The sum of all odd numbers
Input Format
First line contains a single integer n (1 ≤ n ≤ 1000) i.e. total numbers Parth gives.
The next n lines each contain one integer x (1 ≤ x ≤ 1000)
Output Format
Even: sum of even numbers
Odd: sum of odd numbers
Sample Input 0
5
1
2
3
4
5
Sample Output 0
Even: 6
Odd: 9
Sample Input 1
4
2
4
6
8
Sample Output 1
Even: 20
Odd: 0'''
n=int(input())
even=0
odd=0
for i in range(n):
    x=int(input())
    if(x%2==0):
        even+=x
    else:
        odd+=x
print("Even:",even)
print("Odd:",odd)