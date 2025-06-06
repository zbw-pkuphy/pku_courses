is_end=False
case=1
while True:
    positions=[]
    while True:
        position =[int(_) for _ in input().split()]
        if not position:
            break
        if position[0]==0 and position[1]==0:
            is_end=True
            break
        positions.append(position)
    if is_end:
        break
    n,d=positions.pop(0)
    positions.sort(key=lambda x:x[0])
    radars=[]
    ans=0
    for i in range(n):
        x,y=positions[i]
        if y>d:
            ans=-1
            break
        if i==0:
            last=(d**2-y**2)**0.5+x
            radars.append(last)
        else:
            if y**2+(last-x)**2<=d**2:
                pass
            else:
                pre=(d**2-y**2)**0.5+x
                if pre>last:
                    radars.append(last)
                else:
                    radars[-1]=pre
                last=pre
    if ans!=-1:
        ans=len(radars)
    print(f"Case {case}: {ans}")
    case+=1
