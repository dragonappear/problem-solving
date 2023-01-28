# https://www.acmicpc.net/problem/2206
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def bfs():
    dist=[[[-1]*M for _ in range(N)] for _ in range(2)] # (i,j)까지 k개벽을 부수고 도달한 최단거리
    dist[0][0][0]=dist[1][0][0]=1
    q=deque([(0,0,0)])
    while q:
        r,c,k=q.popleft()
        
        if r==N-1 and c==M-1:
            return dist[k][r][c]
        
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            
            if not(0<=nr<N) or not(0<=nc<M) or dist[k][nr][nc]>=0:continue
            
            if graph[nr][nc]==0 and dist[k][nr][nc]==-1:
                dist[k][nr][nc]=dist[k][r][c]+1
                q.append((nr,nc,k))
            
            if  graph[nr][nc]==1 and k==0 and dist[k+1][nr][nc]==-1:  # (nx,ny) 를 부수는 경우
                dist[k+1][nr][nc]=dist[k][r][c]+1
                q.append((nr,nc,k+1))
    return -1

N,M=map(int,input().split())
graph=[ list(map(int,input().strip())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
print(bfs())