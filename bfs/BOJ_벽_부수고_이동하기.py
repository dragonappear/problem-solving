# https://www.acmicpc.net/problem/2206
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

"""
벽을 어떻게 선정할것인가가 포인트인 문제
"""

def bfs(): 
    # dist[0][r][c]: 벽을 하나도 부수지 않고 (r,c)까지 오는데 걸리는 비용
    # dist[1][r][c]: 벽을 하나만 부수고 (r,c)까지 오는데 걸리는 비용, (r,c)가 벽이라서 부수는 경우 포함
    dist = [ [ [-1]*M for _ in range(N)] for _ in range(2)]
    dist[0][0][0]=dist[1][0][0]=1
    
    q=deque([(0,0,0)])
    while q:
        r,c,broken=q.popleft()
        
        if r==N-1 and c==M-1:
            return dist[broken][r][c]
        
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            
            if not(0<=nr<N) or not(0<=nc<M):continue
            
            if graph[nr][nc]==0 and dist[broken][nr][nc]==-1:
                dist[broken][nr][nc]=dist[broken][r][c]+1
                q.append((nr,nc,broken))
            
            # (nx,ny) 를 부수는 경우
            if not broken and graph[nr][nc]==1 and dist[1][nr][nc]==-1:  
                dist[1][nr][nc]=dist[0][r][c]+1
                q.append((nr,nc,1))
                
    return -1


dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
N,M=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]
print(bfs())
