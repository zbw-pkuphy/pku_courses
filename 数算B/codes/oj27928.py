import heapq
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child=[]
def bulif_tree(val,nodes):
    nodes_dict={}
    for i in val:
        nodes_dict[i]=TreeNode(i)
    for i in nodes:
        for j in i[1:]:
            nodes_dict[i[0]].child.append(nodes_dict[j])
            val.remove(j)
    return nodes_dict[val.pop()]
nodes=[]
val=set()
n=int(input())
for i in range(n):
    present=[int(i) for i in input().split()]
    val.add(present[0])
    nodes.append(present)
root=bulif_tree(val,nodes)
def search(root):
    heap=[(root.val,0,root)]
    heapq.heapify(heap)
    for i in root.child:
        heapq.heappush(heap,(i.val,1,i))
    while heap:
        val,_,node=heapq.heappop(heap)
        if _==0:
            print(val)
        else:
            search(node)
search(root)