n=int(input())
tree=[int(_) for _ in input().split()]
if tree[0]>tree[1]:
    max_heap=True
else:
    max_heap=False
is_heap=True
def dfs(node=0,path=[]):
    global is_heap
    path.append(tree[node])
    left=node*2+1
    right=node*2+2
    if left<n:
        if max_heap:
            if not (tree[node]>tree[left] and (right>=n or tree[node]>tree[right])):
                is_heap=False
        else:
            if not (tree[node]<tree[left] and (right>=n or tree[node]<tree[right])):
                is_heap=False              
        if right<n:
            dfs(right)
        dfs(left)
    else:
        print(*path)
    path.pop(-1)
dfs()
if is_heap:
    if max_heap:
        print("Max Heap")
    else:
        print("Min Heap")
else:
    print("Not Heap")