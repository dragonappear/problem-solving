# https://www.acmicpc.net/problem/1926
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def bfs(r:int,c:int)->int:
    graph[r][c]=0
    q=deque([(r,c)])    
    n=0
    while q:
        r,c=q.popleft()
        n+=1
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not(0<=nr<N) or not(0<=nc<M) or not graph[nr][nc]: continue
            graph[nr][nc]=0
            q.append((nr,nc))
    return n
            
N,M=map(int,input().strip().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
count=0
mx=float('-inf')
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            count+=1
            mx = max(mx,bfs(i,j))
    
if mx==float('-inf'): mx=0
write(str(count)+"\n")
write(str(mx)+"\n")