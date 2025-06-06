from collections import defaultdict,deque
n=int(input())
graph=defaultdict(list)
for _ in range(n-1):
    a,b=[int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
visited=set([int(x) for x in input().split()])
ans=0
bfs=deque([0])
while bfs:
    pre=bfs.popleft()
    if pre in visited:
        continue
    ans+=1
    visited.add(pre)
    for child in graph[pre]:
        if child not in visited:
            bfs.append(child)
print(ans)