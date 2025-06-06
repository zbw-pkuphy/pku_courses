N=int(input())
word_set=set()
word_occ={}
for i in range(N):
    string=list(set(input().split()[1:]))
    for j in range(len(string)):
        if string[j] not in word_set:
            word_set.add(string[j])
            word_occ[string[j]]=[i+1]
        else:
            word_occ[string[j]].append(i+1)
M=int(input())
if M==0:
    print(0)
else:
    for i in range(M):
        string=input()
        if string in word_set:
            ans=[str(_) for _ in word_occ[string]] 
            print(" ".join(ans))
        else:
            print("NOT FOUND")
# from collections import defaultdict

# import sys
# input = sys.stdin.read().split()
# ptr = 0
# N = int(input[ptr])
# ptr += 1
# word_occ = defaultdict(list)  # 存储每个单词的行号列表
    
# for line_num in range(1, N + 1):
#     # 解析当前行
#     count = int(input[ptr])
#     ptr += 1
#     words = input[ptr:ptr + count]
#     ptr += count
    
#     # 记录单词出现的行号
#     for word in words:
#         if word not in word_occ:
#             word_occ[word] = [line_num]
#         else:
#                 word_occ[word].append(line_num)
    
# # 查询处理
# M = int(input[ptr])
# ptr += 1

# for _ in range(M):
#     query_word = input[ptr]
#     ptr += 1
    
#     if query_word in word_occ:
#         # 使用集合去重并按顺序输出
#         unique_lines = sorted(list(set(word_occ[query_word])))
#         print(' '.join(map(str, unique_lines)))
#     else:
#         print("NOT FOUND")
