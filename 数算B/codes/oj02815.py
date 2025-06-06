m=int(input())
n=int(input())
table=[[] for _ in range(m)]
max_num=1
count=0
def dfs(i,j,count=0):
    pre_wall=table[i][j]
    table[i][j]=-1
    if pre_wall&1==0 and table[i][j-1]!=-1:
        count+=dfs(i,j-1)
    if pre_wall&2==0 and table[i-1][j]!=-1:
        count+=dfs(i-1,j)
    if pre_wall&4==0 and table[i][j+1]!=-1:
        count+=dfs(i,j+1)
    if pre_wall&8==0 and table[i+1][j]!=-1:
        count+=dfs(i+1,j)
    return count+1
for i in range(m):
    table[i]=[int(_) for _ in input().split()]
for i in range(m):
    for j in range(n):
        if table[i][j]==-1:
            continue
        else:
            count+=1
            max_num=max(max_num,dfs(i,j))
print(count,max_num,sep='\n')