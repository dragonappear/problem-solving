# https://www.acmicpc.net/problem/2606
from sys import stdin,stdout
from collections import defaultdict
input,write=stdin.readline,stdout.write

def dfs(u:int):
    global count
    visit[u],count=True,count+1
    for v in graph[u]:
        if visit[v]: continue
        dfs(v)

V=int(input())
E=int(input())
graph=defaultdict(list)
visit = [False] * (V+1)
count=0
for _ in range(E):
    u,v=map(int,input().split())  
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
write(str(count-1))