'''Meena owns a small but popular bookstore in her town. She maintains a digital record of book prices in the order they arrive. At the end of each day, she sells the last book that arrived (the most recent one) and removes its price from her list.
However, sometimes:
She might sell more than one book at once (for example, if multiple customers buy books together).
If the list becomes empty after sales, she wants her system to display an empty list without errors.
If she tries to remove more books than available, she wants a message: "Not enough books to remove".
Your task is to write a program to help Meena update her list after selling books.
Input Format
A list of integers representing book prices in order of arrival. An integer k → number of books sold (to be removed from the end).
Constraints
1 ≤ length of list ≤ 1000 Each price is a positive integer (1 ≤ price ≤ 10^6). 0 ≤ k ≤ length of list
Output Format

The updated list after removing k books. If k is greater than the length of the list, output: "Not enough books to remove".
Sample Input 0
[100,200,300,400],1
Sample Output 0
[100, 200, 300]
Sample Input 1
[50],1
Sample Output 1
[]'''
books,k=eval(input())
if k>len(books):
    print("Not enough books to remove")
elif k==0:
    print(books)
else:
    print(books[:-k])
