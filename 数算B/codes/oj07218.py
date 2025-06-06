from collections import deque
T=int(input())
def find_S(table):
    for x in range(len(table)):
        for y in range(len(table[0])):
            if table[x][y]=='S':
                return x,y
def bfs(table,x,y,t=1):
    queue=deque()
    queue.append((x,y))
    while queue:
        tmp=deque()
        while queue:
            x,y=queue.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<len(table) and 0<=ny<len(table[0]) and table[nx][ny]!='#':
                    if table[nx][ny]=='E':
                        return t
                    table[nx][ny]='#'
                    tmp.append((nx,ny))
        t+=1
        queue=tmp
    return "oop!"
for __ in range(T):
    R,C=[int(_) for _ in input().split()]
    table=[]
    for x in range(R):
        table.append(list(input()))
    x,y=find_S(table)
    print(bfs(table,x,y))