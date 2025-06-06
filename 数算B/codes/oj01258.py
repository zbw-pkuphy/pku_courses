import heapq,sys
while True:
    try:
        N=int(input())
    except EOFError:
        break
    arr = []
    while len(arr) < N*N:
        line= sys.stdin.readline()
        if not line:
            break
        arr+=list(map(int, line.split()))        
    graph=[]
    for i in range(N):
        start= i*N
        end=start+N
        graph.append(arr[start:end])
    distance=[sys.maxsize]*N
    visited=set()
    start=0
    distance[start]=0
    heap=[(0,start)]
    while heap:
        dist,node=heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if len(visited)==N:
            break
        for i in range(N):
            if graph[node][i]!=0 and i not in visited and graph[node][i]<distance[i]:
                distance[i]=graph[node][i]
                heapq.heappush(heap,(distance[i],i))
    print(sum(distance))