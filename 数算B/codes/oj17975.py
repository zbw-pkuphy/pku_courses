import sys
input = sys.stdin.read
data = input().split()
N,M=int(data[0]),int(data[1])
nums=[int(i) for i in data[2:2+N]]
occupied=[False]*M
num_dic={}
ans=[]
for num in nums:
    j=0
    if num in num_dic.keys():
        ans.append(num_dic[num])
        continue
    h=num%M
    if not occupied[h]:
        ans.append(h)
        occupied[h]=True
        num_dic[num]=h
        continue
    while True:
        j+=1
        h_plus=(num+j**2)%M
        if not occupied[h_plus]:
            ans.append(h_plus)
            occupied[h_plus]=True
            num_dic[num]=h_plus
            break
        h_minus=(num-j**2)%M
        if not occupied[h_minus]:
            ans.append(h_minus)
            occupied[h_minus]=True
            num_dic[num]=h_minus
            break
print(*ans)