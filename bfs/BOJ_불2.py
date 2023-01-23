# https://www.acmicpc.net/problem/5427
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(int(input())):
    M,N=map(int,input().strip().split())
    graph=[list(input().strip()) for _ in range(N)]

    dist1=[ [-1]*M for _ in range(N)]
    dist2=[ [-1]*M for _ in range(N)]
    q1,q2=deque(),deque()
    
    for i in range(N):
        for j in range(M):
            if graph[i][j]=='@':
                q2.append((i,j))
                dist2[i][j]=0
            elif graph[i][j]=='*':
                q1.append((i,j))
                dist1[i][j]=0

    while q1:
        r,c=q1.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not(0<=nr<N) or not(0<=nc<M) or graph[nr][nc]=="#" or dist1[nr][nc]>=0: continue
            dist1[nr][nc]=dist1[r][c]+1
            q1.append((nr,nc))
    
    escape=False
    while q2 and not escape:
        r,c=q2.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            
            if not(0<=nr<N) or not(0<=nc<M):
                write(str(dist2[r][c]+1)+"\n")
                escape=True
                break
            
            if graph[nr][nc]=="#" or dist2[nr][nc]>=0: continue
            if dist1[nr][nc]>=0 and dist1[nr][nc]<=dist2[r][c]+1 : continue
            dist2[nr][nc]=dist2[r][c]+1
            q2.append((nr,nc))
            
    if not escape: write("IMPOSSIBLE\n")