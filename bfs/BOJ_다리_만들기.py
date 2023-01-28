# https://www.acmicpc.net/problem/2146
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def fill():
    visit = [[False] * N for _ in range(N)]
    color=1
    for i in range(N):
        for j in range(N):
            if graph[i][j]==0 or visit[i][j]: continue
            q=deque([(i,j)])
            visit[i][j]=True
            graph[i][j]=color
            while q:
                r,c=q.popleft()
                for dr,dc in dr_dc:
                    nr,nc=r+dr,c+dc
                    if not(0<=nr<N) or not(0<=nc<N) or visit[nr][nc] or graph[nr][nc]==0: continue
                    visit[nr][nc]=True
                    graph[nr][nc]=color
                    q.append((nr,nc))
            color+=1

def get_edges():
    edges=[]
    for i in range(N):
        for j in range(N):
            if graph[i][j]==0: continue
            for dr,dc in dr_dc:
                nr,nc=i+dr,j+dc
                if not(0<=nr<N) or not(0<=nc<N) or graph[nr][nc]>0: continue
                if graph[nr][nc]==0:
                    edges.append((i,j))
                    break
    return edges

def bfs():
    mn=float('inf')
    dist = [[-1] * N for _ in range(N)]
    for r,c in edges:
        dist[r][c]=0
    
    q=deque(edges)
    while q:
        r,c=q.popleft()
        color=graph[r][c]
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not(0<=nr<N) or not(0<=nc<N) or graph[nr][nc]==color: continue
            
            if graph[nr][nc]==0:
                dist[nr][nc]=dist[r][c]+1
                graph[nr][nc]=color
                q.append((nr,nc))
            
            elif graph[nr][nc]!=color:
                mn=min(mn,dist[r][c]+dist[nr][nc])
                break
    return mn

N=int(input())
graph=[list(map(int,input().strip().split())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
fill() # color 표시 O(N^2)
edges=get_edges() # 가장자리 O(N^2)
print(bfs())