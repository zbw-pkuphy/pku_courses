def search(area,n,k,i0=0,j0=-1):
    if k==0:
        return 1
    count=0
    for i in range(i0,n):
        for j in range(j0+1 if i==i0 else 0,n):
            if area[i][j]=="#":
                judge=True
                for _ in range(n):
                    if area[i][_]!="x" and area[_][j]!="x":
                        pass
                    else:
                        judge=False
                        break
                if judge:
                    area[i][j]="x"
                else:
                    continue
                count+=search(area,n,k-1,i,j)
                area[i][j]="#"
    return count
while True:
    n,k=[int(_) for _ in input().split()]
    if n==-1 and k==-1:
        break
    area=[]
    for i in range(n):
        area.append(list(input()))
    
    print(search(area,n,k))