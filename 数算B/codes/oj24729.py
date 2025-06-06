class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child=[]
def buildTree(string):
    if string==None or string[0].isalpha()==False:
        return  
    root=TreeNode(string[0])
    rest=string[2:-1]
    child_string=""
    counter=0
    if rest:
        for index,i in enumerate(rest):
            if i==",":
                continue
            child_string+=i
            if i=="(":
                counter+=1
            elif i==")":
                counter-=1
                if counter==0:
                    root.child.append(buildTree(child_string))
                    child_string=""
            if counter==0 and child_string and (index==len(rest)-1 or rest[index+1]!="("):
                root.child.append(buildTree(child_string))
                child_string=""
    return root
def preorder(root):
    if root:
        print(root.val,end="")
        for i in root.child:
            preorder(i)
def postorder(root):
    if root:
        for i in root.child:
            postorder(i)
        print(root.val,end="")
string=input()
root=buildTree(string)
preorder(root)
print()
postorder(root)