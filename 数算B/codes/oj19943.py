class Vertex:
    def __init__(self,key):
        self.key=key
        self.neighbors={}
    def set_Neighbor(self,other,weight=0):
        self.neighbors[other]=weight
    def get_Neighbor(self):
        return self.neighbors.keys()
class Graph:
    def __init__(self):
        self.vertices={}
    def add_vertex(self,key):
        self.vertices[key]=Vertex(key)
    def add_edge(self,key1,key2,weight=0):
        if key1 not in self.vertices:
            self.add_vertex(key1)
        if key2 not in self.vertices:
            self.add_vertex(key2)
        self.vertices[key1].set_Neighbor(self.vertices[key2],weight)
    def get_edges(self,key):
        return self.vertices[key].get_Neighbor()
    def get_vertices(self):
        return self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.values())
def bulid_laplace_matrix(n,edges):
    g=Graph()
    for v in range(n):
        g.add_vertex(v)
    for edge in edges:
        g.add_edge(edge[0],edge[1])
        g.add_edge(edge[1],edge[0])
    matrix=[]
    for u in g:
        row=[0]*n
        for v in u.neighbors.keys():
            row[v.key]-=1
            row[u.key]=len(u.neighbors)
        matrix.append(row)
    return matrix
n,m=[int(_) for _ in input().split()]
edges=[]
for _ in range(m):
    edges.append(list(map(int,input().split())))
laplace_matrix=bulid_laplace_matrix(n,edges)
for row in laplace_matrix:
    print(*row)
    