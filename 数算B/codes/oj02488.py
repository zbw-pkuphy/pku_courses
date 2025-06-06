n=int(input())
move=((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))
def test(p,q,a,b,step=1):
    if step==p*q:
        return True
    table[a][b]=1
    for dx,dy in move:
        x=a+dx
        y=b+dy
        if x>=0 and x<p and y>=0 and y<q and table[x][y]==0:
            path.append([x,y])
            if test(p,q,x,y,step+1):
                return True
            else:
                path.pop(-1)
    table[a][b]=0
        
for i in range(n):
    p,q=[int(x) for x in input().split()]
    print(f"Scenario #{i+1}:")
    path=[[0,0]]
    table=[[0 for i in range(q)] for j in range(p)]
    test(p,q,0,0)
    ans=""
    if len(path)==p*q:
        for x,y in path:
            ans+=chr(ord('A')+y)+str(x+1)
        print(ans)
    else:
        print("impossible")
    if i!=n-1:
        print("")