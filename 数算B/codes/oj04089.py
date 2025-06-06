class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.child={}
        self.is_end=False
class Tree:
    def __init__(self):
        self.root=TreeNode()
        self.is_correct=True
    def insert(self,number):
        node=self.root
        added=False
        for i in number:
            if i not in node.child.keys():
                node.child[i]=TreeNode(i)
                added=True
            node=node.child[i]
            if node.is_end:
                self.is_correct=False
                return
        if not added:
            self.is_correct=False
        node.is_end=True
    def judge(self,numbers):
        for number in numbers:
            self.insert(number)
            if not self.is_correct:
                return False
        return True
t=int(input())
for i in range(t):
    n=int(input())
    numbers=[]
    for j in range(n):
        numbers.append(input().strip())
    tree=Tree()
    if tree.judge(numbers):
        print("YES")
    else:
        print("NO")