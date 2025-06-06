from collections import deque
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child_node):
        self.children[child_node.value] = child_node
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = GraphNode(value)

    def add_edge(self, value1, value2):
        if value1 not in self.nodes:
            self.add_node(value1)
        if value2 not in self.nodes:
            self.add_node(value2)
        self.nodes[value1].add_child(self.nodes[value2])
        self.nodes[value2].add_child(self.nodes[value1])

    def find_shortest_path(self, start, end):
        if start==end:
            return [start]
        queue = deque([(self.nodes[start], [start])])
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current.value == end:
                return path
            if current.value not in visited:
                visited.add(current.value)
                for child in current.children.values():
                    queue.append((child, path + [child.value]))
        return None
def bulid_graph(words):
    graph = Graph()
    buckets={}
    for word in words:
        for i in range(len(word)):
            bucket=f"{word[:i]}_{word[i+1:]}"
            buckets.setdefault(bucket, set()).add(word)
    for bucket, words in buckets.items():
        for i in words:
            for j in words:
                if i != j:
                    graph.add_edge(i, j)
    return graph
n=int(input())
words = [input() for _ in range(n)]
graph = bulid_graph(words)
start, end = input().split()
if start not in graph.nodes.keys() or end not in graph.nodes.keys():
    print("NO")
else:
    path = graph.find_shortest_path(start, end)
    if path:
        print(" ".join(path))
    else:
        print("NO")