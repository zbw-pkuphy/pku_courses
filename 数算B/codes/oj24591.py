from collections import deque
n=int(input())
for i in range(n):
    operator=deque()
    output=[]
    expression=input().strip()
    m=len(expression)
    j=0
    while j < m:
        if expression[j] in {'+','-','*','/','(',')'}:
            if (expression[j] in {'*','/'} and operator and operator[-1] in {'+','-','('}) or expression[j]=="(":
                operator.append(expression[j])
            elif expression[j]==')':
                while operator[-1] != '(':
                    output.append(operator.pop())
                operator.pop()
            else:
                while operator:
                    if (expression[j] in {'*','/'} and operator and operator[-1] in {'+','-','('}) or(operator and operator[-1]=="("):
                        break
                    output.append(operator.pop())
                operator.append(expression[j])
        else:
            number=str(expression[j])
            while j<m-1 and (expression[j+1].isdigit() or expression[j+1]=='.' ):
                number+=expression[j+1]
                j+=1
            output.append(number)
        j+=1
    while operator:
        top=operator.pop()
        if top:
            output.append(top)
    print(' '.join(output))