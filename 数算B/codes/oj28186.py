from collections import deque
n,m=[int(_) for _ in input().split()]
wanted=[int(_) for _ in input().split()]
queue=deque([])
for i,n in enumerate(wanted):
    queue.append((n,i+1))
while queue:
    pre_num,pre_order=queue.popleft()
    if pre_num<=m:
        continue
    else:
        queue.append((pre_num-m,pre_order))
print(pre_order)