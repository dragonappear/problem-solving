# https://www.acmicpc.net/problem/5567
from sys import stdin,stdout
from collections import defaultdict
input,write=stdin.readline,stdout.write

def dfs(start:int,depth:int):
    global count
    visit[start]=True
    count+=1
    for v in graph[start]:
        if visit[v] or depth>=2 or (start!=1 and v in graph[1]): continue
        dfs(v,depth+1)

N=int(input())
graph=defaultdict(list)
visit = [False] * (N+1)
count=0
for _ in range(int(input())):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
if len(graph[1]):
    dfs(1,0)
    write(str(count-1))
else:
    write(str(count))