# https://www.acmicpc.net/problem/4179
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def OOB(r,c): return True if not(0<=r<R) or not(0<=c<C) else False

R,C=map(int,input().split())
graph=[list(input().strip()) for _ in range(R)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
dist_f,dist_j=[[-1]*C for _ in range(R)],[[-1]*C for _ in range(R)]
q1,q2=deque(),deque()

# 시작 큐 저장
for r in range(R):
    for c in range(C):
        if graph[r][c]=='F':
            q1.append((r,c))
            dist_f[r][c]=0
        elif graph[r][c]=='J':
            q2.append((r,c))
            dist_j[r][c]=0
            
        if graph[r][c]=='#':
            dist_f[r][c]=dist_j[r][c]=0
                    
# 불 BFS
while q1:
    r,c=q1.popleft()
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        if OOB(nr,nc) or dist_f[nr][nc]>=0: continue # 이미 방문한 경우(벽 처리 포함)
        dist_f[nr][nc]=dist_f[r][c]+1
        q1.append((nr,nc))

# 지훈 BFS
while q2:
    r,c=q2.popleft()
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
    
        if OOB(nr,nc): # 탈출 성공한 경우
            write(str(dist_j[r][c]+1)+"\n")
            exit()
    
        if dist_j[nr][nc]>=0: continue # 이미 방문한 경우(벽 처리 포함)
        if dist_f[nr][nc]>=0 and dist_f[nr][nc]<=dist_j[r][c]+1: continue # 불이 먼저 도착해서 도착할 수 없는 경우
        dist_j[nr][nc]=dist_j[r][c]+1
        q2.append((nr,nc))

write("IMPOSSIBLE\n")
