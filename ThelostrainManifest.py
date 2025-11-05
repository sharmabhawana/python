'''n 1920, the kingdom of Zarovia maintained a grand train network connecting distant cities. The chief railway officer maintained a handwritten train manifest listing all compartments attached to each train. However, during a violent storm, some pages were blown away and some compartments were listed multiple times by accident. Worse, the remaining pages were shuffled in reverse order.
The train was scheduled to depart at dawn. The station master needed the official manifest to prevent disasters, but the only copy was the damaged, shuffled list. He called on you, the kingdom’s young programmer, to reconstruct it.
You must remove duplicates (keep first occurrence) and reverse the order of compartments to restore the manifest.
Input Format
First line: n integers — compartment IDs
Constraints
1 ≤ n ≤ 1000 1 ≤ compartment ID ≤ 10^5
Output Format
List of compartment IDs after removing duplicates and reversing
Sample Input 0
10 20 20 30 40 30
Sample Output 0
[40, 30, 20, 10]
Sample Input 1
1 2 3 2 1
Sample Output 1
[3, 2, 1]'''
compartments=list(map(int, input().split()))
seen=set()
unique=[]
for c in compartments:
    if c not in seen:
        unique.append(c)
        seen.add(c)
unique.reverse()
print(unique)
