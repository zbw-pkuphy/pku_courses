def compute_lps(pattern):
    m=len(pattern)
    global lps
    lps = [0] * len(pattern)
    length=0
    for i in range(1,m):
        while length>0 and pattern[i]!=pattern[length]:
            length=lps[length-1]
        if pattern[i]==pattern[length]:
            length+=1
            lps[i]=length
    return lps
def max_circles(text):
    n=len(text)
    lps=compute_lps(text)
    circles=[]
    checked=set()
    for i in range(1,n//2+1):
        if lps[i*2-1]==i:
            for j in range(2,n//i+1):
                if text[:i*j].endswith(text[:i]):
                    if i*j not in checked:
                        circles.append([i*j,j])
                        checked.add(i*j)
                else:
                    break
    return circles
i=1

while True:
    n=int(input())
    if n==0:
        break
    text=input()
    circles=max_circles(text)
    print("Test case #"+str(i))
    for circle in circles:
        print(circle[0],circle[1])
    print("")
    i+=1
