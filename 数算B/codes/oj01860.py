from collections import defaultdict,deque
N,M,S,V=input().split()
N=int(N)
M=int(M)
S=int(S)
V=float(V)
graph=defaultdict(list)
for _ in range(M):
    a,b,r1,c1,r2,c2=input().split()
    a=int(a)
    b=int(b)
    r1=float(r1)
    c1=float(c1)
    r2=float(r2)
    c2=float(c2)
    graph[a].append((b,r1,c1))
    graph[b].append((a,r2,c2))
max_value=[0]*(N+1)
max_value[S]=V
queue=deque([(S,V)])
ans=False
while queue:
    s,v=queue.popleft()
    if max_value[s]>v:
        continue
    if s==S and v>V:
        ans=True
        break
    for e,r1,c1 in graph[s]:
        if max_value[e]<(v-c1)*r1:
            max_value[e]=(v-c1)*r1
            queue.append((e,(v-c1)*r1))
if ans:
    print("YES")
else:
    print("NO")