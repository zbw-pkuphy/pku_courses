import sys
class Treenode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def buildtree(preorder,inorder):
    if len(preorder)==0:
        return None
    root_val=preorder[0]
    root=Treenode(root_val)
    root_index=inorder.index(root_val)
    root.left=buildtree(preorder[1:root_index+1],inorder[:root_index])
    root.right=buildtree(preorder[root_index+1:],inorder[root_index+1:])
    return root
def postorder(root,is_root=0):
    if root==None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val,end='') if is_root==0 else print(root.val)
batch=[]
strings=sys.stdin.readlines()
for line in strings:
    batch.append(line.strip())
    if len(batch)==2:
        root=buildtree(batch[0],batch[1])
        postorder(root,1)
        batch=[]