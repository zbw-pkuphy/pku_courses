def def_matrix(row,col,matrix):
    for i in range(row):
        row=[int(x) for x in input().split()]
        matrix.append(row)
    return None
A,B,C=[],[],[]
row=[0,0,0]
col=[0,0,0]
for i in range(3):
    row[i],col[i]=[int(x) for x in input().split()]
    if i==0:
        def_matrix(row[i],col[i],A)
    elif i==1:
        def_matrix(row[i],col[i],B)
    else:
        def_matrix(row[i],col[i],C)
if row[1]!=col[0] or row[0]!=row[2] or col[1]!=col[2]:
    print("Error!")
else:
    for i in range(row[2]):
        for j in range(col[2]):
            New_num=sum([A[i][x]*B[x][j] for x in range(row[1])])
            C[i][j]+=New_num
            print(C[i][j],end=' ' if j!=col[2]-1 else '\n')