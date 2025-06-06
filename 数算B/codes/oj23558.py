import collections
def dfs(node,depth=0):
    if node not in searched:
        ans.append(node)
        searched.add(node)
    if depth==l:
        return None
    for child in sides[node]:
        if child not in searched:
            dfs(child,depth+1)
n,m,l=map(int,input().split())
sides=collections.defaultdict(list)
for _ in range(m):
    i,j=map(int,input().split())
    sides[i].append(j)
    sides[j].append(i)
for i in range(n):
    sides[i].sort()
root=int(input())
searched={root}
ans=[root]
dfs(root)
print(*ans)