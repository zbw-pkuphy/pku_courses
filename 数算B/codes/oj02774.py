import math
n,k=[int(_) for _ in input().split()]
length=[]
base=[0]*n
for i in range(n):
    length.append(int(input()))
ans=0
if k>sum(length):
    print(0)
else:
    left=1
    right=max(length)
    while left<=right:
        mid=(left+right)//2
        temp=0
        for i in range(n):
            temp+=int(length[i]/mid)
        if temp>=k:
            ans=mid
            left=mid+1
        else:
            right=mid-1
    print(ans)