from collections import defaultdict
import heapq
N,M=map(int,input().split())
graph=defaultdict(list)
for _ in range(M):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))
distance=[float('inf')]*(N+1)
distance[1]=0
queue=[(0,1)]
while queue:
    dist,node=heapq.heappop(queue)
    if dist>distance[node]:
        continue
    for neighbor,weight in graph[node]:
        new_dist=dist+weight
        if new_dist<distance[neighbor]:
            distance[neighbor]=new_dist
            heapq.heappush(queue,(new_dist,neighbor))
print(distance[N])