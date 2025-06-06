M=int(input())
team_accepted={}
team_list=set()
for i in range(M):
    team,problem,is_correct=input().split(",")
    if team not in team_list:
        team_list.add(team)
        team_accepted[team]=[set(),0,0]
    team_accepted[team][1]+=1
    if problem not in team_accepted[team][0] and is_correct=='yes':
        team_accepted[team][0].add(problem)
        team_accepted[team][2]+=1
score=[]
for key,value in team_accepted.items():
    score.append([key,value[1],value[2]])
score.sort(key=lambda x:(-x[2],x[1],x[0]))
for i in range(min(len(score),12)):
    print(i+1,score[i][0],score[i][2],score[i][1])