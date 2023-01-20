# https://www.acmicpc.net/problem/1260
from sys import stdin,stdout
from collections import defaultdict,deque
input,write=stdin.readline,stdout.write

def dfs(u:int):
    visited[u]=True
    write(str(u) + " ")
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            
def dfs2(start:int):
    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]: continue
        visited[u]=True
        write(str(u) + " ")
        for i in range(len(graph[u])-1,-1,-1):
            if visited[graph[u][i]]: continue
            stack.append(graph[u][i])

def bfs(start:int):
    q = deque([start])
    visited[start]=True
    while q:
        u = q.popleft()
        write(str(u) + " ")
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v]=True
    
N,M,V=map(int,input().split())
graph=defaultdict(list)

for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()

visited=[False]*(N+1)    
dfs2(V)
write("\n")
visited=[False]*(N+1)
bfs(V)
write("\n")