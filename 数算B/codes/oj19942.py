rowA,colA,rowB,colB = map(int,input().split())
A,B=[],[]
def input_martrix(row,col,matrix):
    for i in range(row):
        matrix.append(list(map(int,input().split())))
def convolution(rowA,colA,rowB,colB,A,B):
    C=[[0]*(colA-colB+1) for i in range(rowA-rowB+1)]
    for i in range(rowA-rowB+1):
        for j in range(colA-colB+1):
            for k in range(rowB):
                for l in range(colB):
                    C[i][j]+=A[i+k][j+l]*B[k][l]
    return C
input_martrix(rowA,colA,A)
input_martrix(rowB,colB,B)
for row in convolution(rowA,colA,rowB,colB,A,B):
    print(*row)