n=int(input())
used=0
disjoint_set={}
def find(x):
    if  disjoint_set[x]==x:
        return x
    else:
        disjoint_set[x]=find(disjoint_set[x])
        return disjoint_set[x]
differences=[]
for _ in range(n):
    eq=input()
    a,yn,b=eq[0],eq[1],eq[3]
    if a not in disjoint_set.keys():
        disjoint_set[a]=a
    if b not in disjoint_set.keys():
        disjoint_set[b]=b
    if yn=="!":
        differences.append((a,b))
    else:
        parent_a=find(a)
        parent_b=find(b)
        if parent_a!=parent_b:
            disjoint_set[parent_a]=parent_b
def judge():
    for a,b in differences:
        if find(a)==find(b):
            return False
    return True
if judge():
    print(True)
else:
    print(False)