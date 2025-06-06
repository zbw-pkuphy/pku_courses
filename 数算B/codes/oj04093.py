n=int(input())
file_sets=[]
for i in range(n):
    file_sets.append(set(map(int,input().split()[1:])))
def inquiry(file_sets,query):
    include=None
    exclude=set()
    for index in range(len(query)):
        if query[index]==1:
            if not include is None:
                include.intersection_update(file_sets[index])
            else:
                include=file_sets[index].copy()
        elif query[index]==-1:
            exclude.update(file_sets[index])
    if not include:
        return None
    output=include.difference(exclude)
    return output
m=int(input())
for i in range(m):
    query=list(map(int,input().split()))
    ans=inquiry(file_sets,query)
    if ans:
        print(" ".join(map(str,sorted(ans))))
    else:
        print("NOT FOUND")
# n = int(input())
# sets = []
# for _ in range(n):
#     parts = list(map(int, input().split()))
#     ci = parts[0]
#     docs = parts[1:]
#     sets.append(set(docs))

# m = int(input())
# for _ in range(m):
#     query = list(map(int, input().split()))
#     include = [i for i in range(n) if query[i] == 1]
#     # 计算必须包含的集合的交集
#     if not include:
#         print("NOT FOUND")
#         continue
#     s = sets[include[0]].copy()
#     for i in include[1:]:
#         s.intersection_update(sets[i])
#         if not s:
#             break
#     if not s:
#         print("NOT FOUND")
#         continue
#     # 处理必须排除的集合
#     exclude = [i for i in range(n) if query[i] == -1]
#     for i in exclude:
#         s.difference_update(sets[i])
#         if not s:
#             break
#     if not s:
#         print("NOT FOUND")
#     else:
#         print(' '.join(map(str, sorted(s))))