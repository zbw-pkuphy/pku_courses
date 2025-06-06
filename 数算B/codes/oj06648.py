import heapq
T=int(input())
def refresh(min_sum,temp):
    n=len(temp)
    heap0=[]
    new_sum=[]
    for i in range(len(min_sum)):
        heapq.heappush(heap0, (min_sum[i]+temp[0], i, 0))
    while len(new_sum)<n and heap0:
        val,i,j = heapq.heappop(heap0)
        new_sum.append(val)
        if j+1 < n:
            heapq.heappush(heap0,(min_sum[i]+temp[j+1],i,j+1))
        
    return new_sum
for i in range(T):
    m,n=map(int,input().split())
    for j in range(m):
        if j==0:
            min_sum=sorted([int(x) for x in input().split()])
            heapq.heapify(min_sum)
        else:
            temp=sorted([int(x) for x in input().split()])
            min_sum=refresh(min_sum,temp)
    print(*min_sum)