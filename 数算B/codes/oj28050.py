class Graph:
    def __init__(self):
        self.vertices={}
        self.num_vertices=0
    def add_vertex(self,key):
        self.num_vertices+=1
        new_vertex=Vertex(key)
        self.vertices[key]=new_vertex
        return new_vertex
    def get_vertex(self,key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None
    def add_edge(self,f,t):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t])
        self.vertices[t].add_neighbor(self.vertices[f])
    def get_vertices(self):
        return self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.values())
    
class Vertex:
    def __init__(self,num):
        self.key=num
        self.neighbors=set()
        self.visited=False
    def __lt__(self,other):
        return self.key<other.key
    def add_neighbor(self,neighbor):
        self.neighbors.add(neighbor)
    def get_neighbors(self):
        return self.neighbors
def next_legal_steps(size,row,col):
    steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    legal_steps=[]
    for step in steps:
        new_row=row+step[0]
        new_col=col+step[1]
        if 0<=new_row<size and 0<=new_col<size:
            legal_steps.append((new_row,new_col))
    return legal_steps
def knight_graph(size):
    graph=Graph()
    for row in range(size):
        for col in range(size):
            id=row*n+col
            new_postions=next_legal_steps(size,row,col)
            for pos in new_postions:
                nid=pos[0]*n+pos[1]
                graph.add_edge(id,nid)
    return graph
def order_avaliable(n):
    res_list = []
    for v in n.get_neighbors():
        if v.visited==False:
            c=0
            for w in v.get_neighbors():
                if w.visited==False:
                    c += 1
            res_list.append((c,v))
    res_list.sort(key=lambda x:x[0])
    return [y[1] for y in res_list]

def knight_tour(lenth,path,pre,max_length):
    if lenth==max_length:
        return True
    path.append(pre)
    pre.visited=True
    ordered_neighbors=order_avaliable(pre)
    for next_node in ordered_neighbors:
        if next_node.visited==False and knight_tour(lenth+1,path,next_node,max_length):
            return True
    pre.visited=False
    path.pop()
    return False
n=int(input())
sr,sc=[int(_) for _ in input().split()]
graph=knight_graph(n)
if knight_tour(1,[],graph.get_vertex(sr*n+sc),n*n):
    print("success")
else:
    print("fail")