import heapq
import sys
class Node:
    def __init__(self, val,weight):
        self.val = val
        self.weight=weight
        self.left = None
        self.right = None
    def __lt__(self, other):
        if self.weight == other.weight:
            return self.val<other.val
        else: 
            return self.weight<other.weight
def build_huffman_tree(arr):
    heap = []
    for val,weight in arr:
        heapq.heappush(heap,Node(val,weight))
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        merged=Node(min(left.val,right.val),left.weight+right.weight)
        heapq.heappush(heap,merged)
        merged.left=left
        merged.right=right
    return heap[0]
def encode_dict(root):
    codes={}
    def dfs(root,code):
        if root.left is None and root.right is None:
            codes[root.val]=code
            return
        dfs(root.left,code+'0')
        dfs(root.right,code+'1')
    dfs(root,'')
    return codes
def huffman_encode(codes, s):
    return ''.join([codes[i] for i in s])
def huffman_decode(root, s):
    decoded=""
    node=root
    for i in s:
        if i=='0':
            node=node.left
        else:
            node=node.right
        if node.left is None and node.right is None:
            decoded+=str(node.val)
            node=root
    return decoded
n=int(sys.stdin.readline().strip())
arr=[]
for i in range(n):
    val,weight=sys.stdin.readline().strip().split()
    arr.append((val,int(weight)))
root=build_huffman_tree(arr)
codes=encode_dict(root)
for s in sys.stdin:
    s=s.strip()
    if s[0] in {"0","1"}:
        print(huffman_decode(root,s))
    else:
        print(huffman_encode(codes,s))
