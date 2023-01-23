# https://www.acmicpc.net/problem/4179
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write
  
R,C=map(int,input().split())
graph=[list(input().strip()) for _ in range(R)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
dist1 = [[-1] * C for _ in range(R)]
dist2 = [[-1] * C for _ in range(R)]
q1,q2=deque(),deque()

for i in range(R):
    for j in range(C):
        if graph[i][j]=='F':
            dist1[i][j]=0
            q1.append((i,j))
        elif graph[i][j]=='J':
            dist2[i][j]=0
            q2.append((i,j))

# 불 BFS
while q1:
    r,c=q1.popleft()
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        if not(0<=nr<R) or not(0<=nc<C): continue
        if dist1[nr][nc]>=0 or graph[nr][nc]=="#": continue
        dist1[nr][nc]=dist1[r][c]+1
        q1.append((nr,nc))

# J BFS
while q2:
    r,c=q2.popleft()
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        
        if not(0<=nr<R) or not(0<=nc<C):
            write(str(dist2[r][c]+1)+"\n")
            exit()
        
        if dist2[nr][nc]>=0 or graph[nr][nc]=="#": continue
        if dist1[nr][nc]!=-1 and dist1[nr][nc]<=dist2[r][c]+1 : continue
        dist2[nr][nc]=dist2[r][c]+1
        q2.append((nr,nc))

write("IMPOSSIBLE\n")