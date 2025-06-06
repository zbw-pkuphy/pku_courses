n=int(input())
operations=[]
for _ in range(2*n):
    operations.append(input().split())
stack=[]
removed=0
ans=0
for i in range(2*n):
    if operations[i][0]=="add":
        stack.append(int(operations[i][1]))
    else:
        removed+=1
        if stack[-1]!=removed:
            stack.sort(key=lambda x:-x)
            ans+=1
        stack.pop(-1)
print(ans)
