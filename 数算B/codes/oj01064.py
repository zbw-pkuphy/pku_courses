N,K=[int(_) for _ in input().split()]
nums=[]
for _ in range(N):
    nums.append(int(float(input())*100))
left=1
right=max(nums)
ans=0
while left<=right:
    mid=(left+right)//2
    sum_up=0
    for num in nums:
        sum_up+=num//mid
    if sum_up<K:
        right=mid-1
    else:
        ans=mid
        left=mid+1
print(f"{ans/100:.2f}")