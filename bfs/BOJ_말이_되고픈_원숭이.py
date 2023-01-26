# https://www.acmicpc.net/problem/1600
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write


K=int(input())
W,H=map(int,input().split())
board=[list(map(int,input().strip().split())) for _ in range(H)]

dist= [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
q=deque([(0,0,0)])

dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
dh=[(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]

while q:
    r,c,k=q.popleft()
    
    if r==H-1 and c==W-1:
        print(dist[r][c][k])
        exit()
    
    if k<K:
        for dr,dc in dh:
            nr,nc=r+dr,c+dc
            if not(0<=nr<H) or not(0<=nc<W) or board[nr][nc]==1 or dist[nr][nc][k+1]>0: continue
            dist[nr][nc][k+1]=dist[r][c][k]+1
            q.append((nr,nc,k+1))
        
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        if not(0<=nr<H) or not(0<=nc<W) or board[nr][nc]==1 or dist[nr][nc][k]>0: continue
        dist[nr][nc][k]=dist[r][c][k]+1
        q.append((nr,nc,k))

print(-1)