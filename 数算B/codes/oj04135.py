N,M=[int(_) for _ in input().split()]
spend=[]
for _ in range(N):
    spend.append(int(input()))
def check(mid):
    count=1
    cur=0
    for i in range(N):
        if spend[i]>mid:
            return False
        if cur+spend[i]>mid:
            count+=1
            cur=spend[i]
            if count>M:
                return False
        else:
            cur+=spend[i]
    return True
left=max(spend)
right=sum(spend)
ans=right
while left<=right:
    mid=(left+right)//2
    if check(mid):
        right=mid-1
        ans=mid
    else:
        left=mid+1
print(ans)