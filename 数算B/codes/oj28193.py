n,m=[int(_) for _ in input().split()]
cost=[int(_) for _ in input().split()]
disjoint_set=[i for i in range(n+1)]
def find(x):
    if  disjoint_set[x]==x:
        return x
    else:
        disjoint_set[x]=find(disjoint_set[x])
        return disjoint_set[x]
for _ in range(m):
    a,b=[int(_) for _ in input().split()]
    parent_a=find(a)
    parent_b=find(b)
    if cost[parent_a-1]>cost[parent_b-1]:
        disjoint_set[parent_a]=parent_b
    else:
        disjoint_set[parent_b]=parent_a
visited=set()
ans=0
for i in range(1,n+1):
    parent=find(i)
    if parent in visited:
        continue
    else:
        ans+=cost[parent-1]
        visited.add(parent)
print(ans)