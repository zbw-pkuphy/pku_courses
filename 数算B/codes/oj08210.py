L,N,M=[int(_) for _ in input().split()]
rock_location=[]
for i in range(N):
    rock_location.append(int(input()))
rock_location.append(L)
left=0
right=L//(N-M+1)
while left<=right:
    last=0
    count=0
    mid=(left+right)//2
    for cur in rock_location:
        if cur-last>=mid:
            last=cur
        else:
            count+=1
    if count>M:
        right=mid-1
    else:
        best=mid
        left=mid+1
print(best)