# https://www.acmicpc.net/problem/10026
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def bfs():
    a=0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]: continue
            
            visit[i][j]=True
            a+=1
            ch=graph[i][j]
            q=deque([(i,j)])
            while q:
                r,c=q.popleft()
                for dr,dc in dr_dc:
                    nr,nc=r+dr,c+dc
                    if not(0<=nr<N) or not(0<=nc<N) or visit[nr][nc] or graph[nr][nc]!=ch: continue 
                    visit[nr][nc]=True
                    q.append((nr,nc))
    return a

N=int(input())
graph=[list(input().strip()) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]

normal=bfs()

for i in range(N):
    for j in range(N):
        if graph[i][j]=='G': graph[i][j]='R'

abnormal=bfs()

print(normal,abnormal)

            