# https://www.acmicpc.net/problem/11403
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def dfs(start,u:int):
    for v in range(N):
        if not graph[u][v] or visit[v]: continue
        visit[v]=True
        result[start][v]=1
        dfs(start,v)
        
N=int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
result= [[0]*N for _ in range(N)]
for i in range(N):
    visit=[False]*N
    dfs(i,i)

for r in result:
    write(' '.join(map(str,r ))+"\n")