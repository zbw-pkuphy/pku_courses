from collections import defaultdict,deque
n,m=[int(_) for _ in input().split()]
graph=defaultdict(list)
indegree=[0]*n
for _ in range(m):
    a,b=[int(_) for _ in input().split()]
    graph[b].append(a)
    indegree[a]+=1
queue=deque()
reward=[100]*n
for i in range(n):
    if indegree[i]==0:
        queue.append((100,i))
while queue:
    pre_reward,pre=queue.popleft()
    for nxt in graph[pre]:
        indegree[nxt]-=1
        reward[nxt]=max(reward[nxt],pre_reward+1)
        if indegree[nxt]==0:
            queue.append((reward[nxt],nxt))
print(sum(reward))