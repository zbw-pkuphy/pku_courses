from collections import deque
class Node:
    def __init__(self,val):
        self.children=[]
        self.val=val
def bulid_tree(vals):
    root,child_num=Node(vals[0][0]),vals[0][1]
    queue=deque([[root,child_num]])
    index=1
    while queue:
        tmp=[]
        for _ in range(len(queue)):
            node,child_num=queue.popleft()
            for _ in range(child_num):
                pre=Node(vals[index][0])
                node.children.append(pre)
                tmp.append([pre,vals[index][1]])
                index+=1
        queue.extend(tmp)
    return root
def post_root(root):
    if not root:
        return
    for child in root.children:
        post_root(child)
    ans.append(root.val)
    return 
n=int(input())
ans=[]
for _ in range(n):
    a=input().split()
    vals=[]
    childrens=[]
    nodes=[]
    for i in range(len(a)//2):
        vals.append([a[i*2],int(a[i*2+1])])
    root=bulid_tree(vals)
    post_root(root)
print(*ans)