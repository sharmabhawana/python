'''A train is about to leave the station. Each compartment of the train has a unique compartment number, and they are stored in a list in order of attachment. Suddenly, railway officials decide to add a new compartment x at a given position p.
But before updating the list, the following rules must be followed:
Valid Position Check
If p is within the list range, insert the compartment at that position (shift the rest to the right).
If p equals the length of the list, add the compartment at the end.
If p is greater than the length of the list, output: "Invalid position".
Uniqueness Check
If x already exists in the list, officials reject it. Output: "Compartment already exists".
Special Compartment Rule
If the new compartment number x is 0, it is considered a special engine compartment and must always be added at the front (position 0), regardless of the given p.
Empty Train Rule
If the train has no compartments, the new compartment becomes the first compartment, no matter what p is.
Input Format
A list of integers representing compartment numbers. An integer x → the new compartment number. An integer p → the position to insert the compartment.
Constraints
0 ≤ length of list ≤ 1000 0 ≤ x ≤ 10^6 0 ≤ p ≤ length of list
Output Format
The updated list after insertion, Or an error message if insertion is not possible.
Sample Input 0
[1,2,3,4],5,2
Sample Output 0
[1, 2, 5, 3, 4]
Sample Input 1
[10,20,30],25,1
Sample Output 1
[10, 25, 20, 30]'''
t,x,p=eval(input())
if len(t)==0:
    t.append(x)
    print(t)
elif x in t:
    print("Compartment already exists")
elif x==0:
    t.insert(0,x)
    print(t)
elif p>len(t):
    print("Invalid position")
else:
    t.insert(p, x)
    print(t)
