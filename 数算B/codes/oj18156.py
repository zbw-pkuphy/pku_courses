import math
def find(T,S):
    S.sort()
    left,right=0,len(S)-1
    closest=math.inf
    while left<right:
        pre=S[left]+S[right]
        diff=pre-T
        if abs(diff)<abs(closest-T):
            closest=pre
        elif abs(diff)==abs(closest-T):
            if pre<closest:
                closest=pre
        if diff<0:
            left+=1
        else:
            right-=1
    return closest
T=int(input())
S=[int(_) for _ in input().split()]
print(find(T,S))