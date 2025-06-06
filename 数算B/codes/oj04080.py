import heapq
def min_weighted_path_length(weights):
    heapq.heapify(weights)
    total=0
    while len(weights)>1:
        left=heapq.heappop(weights)
        right=heapq.heappop(weights)
        combined=left+right
        total+=combined
        heapq.heappush(weights,combined)
    return total
n=int(input())
weights=[int(i) for i in input().split()]
print(min_weighted_path_length(weights))