R,C=map(int,input().split())
h=[[int(_) for _ in input().split()] for __ in range(R)]
height=[]
for i in range(R):
    for j in range(C):
        height.append((h[i][j],i,j))
height.sort()
dp=[[1]*C for _ in range(R)]
for val,i,j in height:
    max_len=1
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=i+dx<R and 0<=j+dy<C and h[i+dx][j+dy]<val:
            max_len=max(max_len,dp[i+dx][j+dy]+1)
    dp[i][j]=max_len
ans=0
for i in range(R):
    for j in range(C):
        ans=max(ans,dp[i][j])
print(ans)