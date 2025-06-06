import math
n=int(input())
nodes=[int(_) for _ in input().split()]
max_value=[[nodes[_],0] for _ in range(n)]
for i in range(n-1,-1,-1):
    left=2*i+1
    right=2*i+2
    if left<n:
        max_value[i][0]+=max_value[left][1]
        max_value[i][1]+=max(max_value[left])
    if right<n:
        max_value[i][0]+=max_value[right][1]
        max_value[i][1]+=max(max_value[right])
print(max(max_value[0]))