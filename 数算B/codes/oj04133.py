d=int(input())
n=int(input())
trash=[]
for i in range(n):
    trash.append([int(_) for _ in input().split()])
num=0
maxnum=-1
ans=0
locations=set()
for index,i in enumerate(trash):
    num=i[2]
    x,y=i[0],i[1]
    for j in range(max(0,x-d),min(1025,x+d+1)):
        for k in range(max(0,y-d),min(1025,y+d+1)):
            if j+10000*k in locations:
                continue
            locations.add(j+1000*k)
            for other in trash[index+1:]:
                if abs(other[0]-j)<=d and abs(other[1]-k)<=d:
                    num+=other[2]
            if num>maxnum:
                maxnum=num
                ans=1
            elif num==maxnum:
                ans+=1
            num=i[2]
print(ans,maxnum)