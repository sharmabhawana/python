'''At WonderWorld Theme Park, visitors are lined up for the grand roller coaster ride of the day. Everyone expects the usual "first come, first serve," but the manager announces a fun twist:
First, the queue will be reversed, so those who came last will ride first.
Then, to spice things up, he decides that only every alternate visitor in this reversed list will get on the ride in the first round.
The rest will wait for the next ride. Now, the park staff wants a program to determine the final boarding order after applying both rules.
Input Format
A single line containing space-separated integers, representing the visitor token IDs in the original queue.
Constraints
1 ≤ N ≤ 10⁵, where N is the number of visitors. 1 ≤ Token ID ≤ 10⁶ Input list may contain distinct or repeated token IDs.
Output Format
A list (in Python list format) representing the final ride order after reversing the queue and selecting every alternate visitor.
Sample Input 0
1 2 3 4
Sample Output 0
[4, 2]
Sample Input 1
10 20 30
Sample Output 1
[30, 10]'''
t=list(map(int,input().split()))
t.reverse()
final=t[::2]
print(final)