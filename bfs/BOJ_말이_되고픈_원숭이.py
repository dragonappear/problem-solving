# https://www.acmicpc.net/problem/1600
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def bfs():
    def OOB(nr,nc): return True if not(0<=nr<N) or not(0<=nc<M) else False
    dist=[[[-1]*M for _ in range(N)] for _ in range(K+1)] # dist[k][i][j]: (i,j)까지 k번 사용해서 도달한 최단거리
    dist[0][0][0]=0
    q=deque([(0,0,0)])
        
    while q:
        r,c,k=q.popleft()
        
        if r==N-1 and c==M-1:
            return dist[k][r][c]
        
        if k<K:            
            for dr,dc in dh:
                nr,nc=r+dr,c+dc
                if OOB(nr,nc) or graph[nr][nc]==1 or dist[k+1][nr][nc]>=0: continue
                dist[k+1][nr][nc]=dist[k][r][c]+1
                q.append((nr,nc,k+1))
        
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if OOB(nr,nc) or graph[nr][nc]==1 or dist[k][nr][nc]>=0: continue
            dist[k][nr][nc]=dist[k][r][c]+1
            q.append((nr,nc,k))
    return -1

K=int(input())
M,N=map(int,input().split())
graph=[list(map(int,input().split()))  for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
dh=[(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
print(bfs())
