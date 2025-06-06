count=1
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    religion=[{i} for i in range(1,n+1)]
    religions={}
    religion_num=n
    for i in range(n):
        religions[i]=i
    for i in range(m):
        a,b=map(int,input().split())
        if religions[a-1]!=religions[b-1]:
            religion_b=religion[religions[b-1]]
            religion[religions[a-1]]=religion[religions[a-1]]|(religion_b)
            religion_num-=1
            for j in religion_b:
                religions[j-1]=religions[a-1]
            religion_b.clear()
    print(f"Case {count}: {religion_num}")
    count+=1

#ai,much better:
# def find(x, parent):
#     if parent[x] != x:
#         parent[x] = find(parent[x], parent)
#     return parent[x]

# def union(x, y, parent):
#     fx = find(x, parent)
#     fy = find(y, parent)
#     if fx != fy:
#         parent[fy] = fx

# def main():
#     import sys
#     input_data = sys.stdin.read().splitlines()
#     case_num = 1
#     i = 0
#     while i < len(input_data):
#         # 读取每组数据的第一行，n为学生数，m为询问对数
#         if input_data[i].strip() == "":
#             i += 1
#             continue
#         parts = input_data[i].split()
#         n = int(parts[0])
#         m = int(parts[1])
#         if n == 0 and m == 0:
#             break
#         i += 1
        
#         # 初始化每个学生的父节点为自己
#         parent = [j for j in range(n + 1)]
        
#         # 处理后续的m行数据
#         for _ in range(m):
#             a, b = map(int, input_data[i].split())
#             union(a, b, parent)
#             i += 1

#         # 统计有多少个独立集合
#         religions = set()
#         for j in range(1, n + 1):
#             religions.add(find(j, parent))
#         print(f"Case {case_num}: {len(religions)}")
#         case_num += 1

# if __name__ == '__main__':
#     main()
