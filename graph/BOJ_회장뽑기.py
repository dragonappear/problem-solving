# https://www.acmicpc.net/problem/2660
from sys import stdin,stdout
from collections import defaultdict
input,write=stdin.readline,stdout.write

def dfs(u:int,depth:int):
    for v in graph[u]:
        if depth+1 < score[v]: 
            score[v]=depth+1
            dfs(v,depth+1)
        
N=int(input())
graph=defaultdict(list)
while True:
    u,v=map(int,input().split())
    if (u,v)==(-1,-1): break
    graph[u].append(v)
    graph[v].append(u)

result=[0]*(N+1)
for i in range(1,N+1):
    score=[float('inf')]*(N+1)
    score[0]=score[i]=0
    dfs(i,0)
    result[i]=max(score)

result=[(result[i],i) for i in range(1,N+1)]
result.sort()
score=result[0][0]
count=sum( 1 for r in result if r[0]==score)
candidates=list( r[1] for r in result if r[0]==score)

write(str(score) + " " + str(count)+"\n")
write(' '.join(map(str,candidates)))

    