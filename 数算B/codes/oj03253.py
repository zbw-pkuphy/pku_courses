from collections import deque
while True:
    ans=[]
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    queue=deque([i for i in range(1,n+1)])
    for i in range(p-1):
        queue.append(queue.popleft())
    while queue:
        for i in range(m-1):
            queue.append(queue.popleft())
        ans.append(str(queue.popleft()))
    print(','.join(ans))