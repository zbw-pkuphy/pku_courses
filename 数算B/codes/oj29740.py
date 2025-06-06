from collections import defaultdict
n,p=[int(_) for _ in input().split()]
node=[[0,0]]
graph=defaultdict(dict)
indegree=[0]*(n+1)
outdegree=[0]*(n+1)
queue=[]
for _ in range(n):
    node.append([int(_) for _ in input().split()])
for _ in range(p):
    a,b,w=[int(_) for _ in input().split()]
    if b in graph[a].keys():
        graph[a][b]+=w
    else:
        graph[a][b]=w
        indegree[b]+=1
        outdegree[a]+=1
ans_1=[]
for _ in range(1,n+1):
    if indegree[_]==0:
        queue.append(_)
    if outdegree[_]==0:
        ans_1.append(_)
while queue:
    tmp=[]
    while queue:
        pre=queue.pop(0)
        if node[pre][0]<0:
            node[pre][0]=0
        for child in graph[pre].keys():
            indegree[child]-=1
            node[child][0]+=graph[pre][child]*node[pre][0]
            if indegree[child]==0:
                node[child][0]-=node[child][1]
                tmp.append(child)
    if tmp:
        queue=tmp[:]
ans_1.sort()
ans=[]
for i in ans_1:
    if node[i][0]>0:
        ans.append([i,node[i][0]])
if not ans or max(indegree)>0:
    print("NULL")
else:
    for row in ans:
        print(*row)