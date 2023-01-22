# https://www.acmicpc.net/problem/7576
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

M,N=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
dist=[[0] * M for _ in range(N)]
q=deque()

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            dist[i][j]=-1
        elif graph[i][j]==1:
            q.append((i,j))

while q:
    r,c=q.popleft()
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        if not(0<=nr<N) or not(0<=nc<M) or dist[nr][nc]>=0: continue
        dist[nr][nc]=dist[r][c]+1
        q.append((nr,nc))

mx = float('-inf')
for i in range(N):
    for j in range(M):
        if dist[i][j]==-1:
            write("-1\n")
            exit()
        mx = max(mx,dist[i][j])

write(str(mx)+"\n")