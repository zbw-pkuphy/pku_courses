from collections import deque
coded=input()
decoded=""
stack=deque()
strings=[]
num=[]
for index,i in enumerate(coded):
    if i=="[":
        stack.append(i)
        while coded[index+1].isdigit()==True:
            num.append(coded[index+1])
            index+=1
        stack.append("".join(num))
        num=[]
    elif i!="]" and i.isdigit()==False:
        stack.append(i)
    elif i=="]":
        while stack[-1].isdigit()==False:
            strings.append(stack.pop())
        times=int(stack.pop())
        stack.pop()
        string="".join(strings[::-1])
        stack.append(string*times)
        strings=[]
decoded="".join(stack)
print(decoded)

