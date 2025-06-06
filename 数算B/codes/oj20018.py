ans=0
def merge_sort(arr):
    global ans
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    global ans
    sorted_arr=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]>=right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            ans+=len(left)-i
            j+=1
    if j==len(right):
        sorted_arr.extend(left[i:])
    else:
        sorted_arr.extend(right[j:])
    return sorted_arr
N=int(input())
bugs=[]#此bug非彼bug
for i in range(N):
    bugs.append(int(input()))
merge_sort(bugs)
print(ans)