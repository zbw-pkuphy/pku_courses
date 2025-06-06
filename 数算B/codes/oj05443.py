import heapq
def dijkstra(graph,start,end):
    distances = {vertex: float('infinity') for vertex in graph.keys()}
    distances[start] = 0
    path= {vertex: None for vertex in graph.keys()}
    path[start]=start
    priority_queue=[(0,start)]
    while priority_queue:
        current_distance,current_vertex= heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor,weight in graph[current_vertex]:
            distance = current_distance + int(weight)
            if distance < distances[neighbor]:
                path[neighbor]=path[current_vertex]+f"->({weight})->{neighbor}"
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance,neighbor))
    if distances[end]==float('infinity'):
        return False
    else:
        return path[end]
P=int(input())
graph={}
for _ in range(P):
    graph[input()]=set()
Q=int(input())
for _ in range(Q):
    a,b,w=input().split()
    graph[a].add((b,w))
    graph[b].add((a,w))
R=int(input())
for _ in range(R):
    start,end=input().split()
    print(dijkstra(graph,start,end))

