# https://www.acmicpc.net/problem/2573
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def melt():
    visit=[[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0: continue
            
            visit[i][j]=True
            for dr,dc in dr_dc:
                nr,nc=i+dr,j+dc
                if visit[nr][nc]: continue # 이미 방문했다면 넘어가기
                if graph[nr][nc]==0 and graph[i][j]>=1:
                    graph[i][j]-=1

def bfs():
    ice_cnt=0
    x,y=0,0
    for i in range(N):
        for j in range(M):
            if graph[i][j]>0: 
                ice_cnt+=1
                x,y=i,j
    
    if ice_cnt==0: return 0 # 다 녹았을때
    
    q=deque([(x,y)])
    visit=[[False]*M for _ in range(N)]
    visit[x][y]=True
    surr_cnt=0
    while q:
        r,c=q.popleft()
        surr_cnt+=1
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if visit[nr][nc] or graph[nr][nc]==0: continue
            visit[nr][nc]=True
            q.append((nr,nc))
            
    if ice_cnt>surr_cnt: return -1 # 두덩이이상으로 분리되었을때
    elif ice_cnt==surr_cnt: return 1 # 한덩이일때
    
def solve():
    year=0
    while True:
        year+=1
        melt()
        rst=bfs()
        if rst==0: return 0
        elif rst==-1: return year

N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
print(solve())