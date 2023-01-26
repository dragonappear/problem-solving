# https://www.acmicpc.net/problem/2146
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def classify(graph):
    num=0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] or graph[i][j]==0: continue
            num+=1
            visit[i][j]=True
            graph[i][j]=num
            q=deque([(i,j)])
            while q:
                r,c=q.popleft()
                for dr,dc in dr_dc:
                    nr,nc=r+dr,c+dc
                    if not(0<=nr<N) or not(0<=nc<N) or visit[nr][nc] or graph[nr][nc]==0: continue
                    visit[nr][nc]=True
                    graph[nr][nc]=num
                    q.append((nr,nc))

N=int(input())
board=[list(map(int,input().strip().split())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
classify(board) # O(N^2)
mn=float('inf')
dist=[[-1]*N for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(N):
        if board[i][j]==0: continue
        q.append((i,j))
        dist[i][j]=0
    
while q:
    r,c=q.popleft()
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        if not(0<=nr<N) or not(0<=nc<N) or board[nr][nc]==board[r][c]: continue # 인덱스 범위를 벗어나거나 같은 섬일 경우
        
        if board[nr][nc]!=0: # 인접한 섬이 아닐 경우
            mn=min(mn,dist[nr][nc]+dist[r][c]) # (r,c) 와 (nr,nc) 각각이 육지로부터 떨어진 거리를 더하면 된다
        else: # 바다일 경우
            board[nr][nc]=board[r][c]
            dist[nr][nc]=dist[r][c]+1
            q.append((nr,nc))

print(mn)
    