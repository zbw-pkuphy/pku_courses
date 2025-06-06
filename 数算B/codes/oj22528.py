import math
nums=[float(_) for _ in input().split()]
nums.sort()
n=len(nums)
A_num=nums[int(n*0.4)]
left=0
right=1000000000
ans=-1
while left<=right:
    mid=(left+right)//2
    a=mid/1000000000
    if a*A_num+1.1**(a*A_num)<85:
        left=mid+1
    else:
        ans=mid
        right=mid-1
print(ans)