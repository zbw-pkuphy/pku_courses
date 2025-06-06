T=int(input())
def find(x,y,count,ways=0,pre=1):
    if pre==m*n:
        return 1
    ways=0
    mov=[[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
    moved=False
    for i in mov:
        if 0<=x+i[0]<n and 0<=y+i[1]<m and count[x+i[0]][y+i[1]]==0:
            count[x+i[0]][y+i[1]]=1
            moved=True
            ways+=find(x+i[0],y+i[1],count,ways,pre+1)
            count[x+i[0]][y+i[1]]=0
    if not moved:
        return 0
    return ways
        
for _ in range(T):
    n,m,x,y=[int(i) for i in input().split()]
    count=[[0 for _ in range(m)] for _ in range(n)]
    count[x][y]=1
    print(find(x,y,count))

