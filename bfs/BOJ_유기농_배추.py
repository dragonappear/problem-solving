# https://www.acmicpc.net/problem/1012
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(int(input())):
    M,N,K=map(int,input().split())
    graph=[[0]* M for _ in range(N)]
    for _ in range(K):
        c,r=map(int,input().split())
        graph[r][c]=1
    
    count=0
    q=deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                count+=1
                graph[i][j]=0
                q.append((i,j))
                while q:
                    r,c=q.popleft()
                    for dr,dc in dr_dc:
                        nr,nc=r+dr,c+dc
                        if not(0<=nr<N) or not(0<=nc<M) or not graph[nr][nc]:continue
                        graph[nr][nc]=0
                        q.append((nr,nc))
    
    write(str(count)+"\n")