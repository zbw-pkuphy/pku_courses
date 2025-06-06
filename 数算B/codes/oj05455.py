import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BineraySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,node, val):
        if not node:
            self.root=TreeNode(val)
            return
        if val<node.val:
            if node.left:
                self.insert(node.left,val)
            else:
                node.left=TreeNode(val)
        elif val>node.val:
            if node.right:
                self.insert(node.right,val)
            else:
                node.right=TreeNode(val)
    def build(self,nums):
        for num in nums:
            self.insert(self.root,num)
    def levelorder(self):
        if not self.root:
            return []
        queue=[self.root]
        ans=[]
        while queue:
            node=queue.pop(0)
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
nums=[int(i) for i in input().split()]
Tree=BineraySearchTree()
Tree.build(nums)
root=Tree.root
print(*Tree.levelorder())