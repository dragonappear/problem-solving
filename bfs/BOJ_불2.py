# https://www.acmicpc.net/problem/5427
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def OOB(r,c): return True if not(0<=r<H) or not(0<=c<W) else False

for _ in range(int(input())):
    W,H=map(int,input().split())
    graph=[list(input().strip()) for _ in range(H)]
    dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
    dist_f,dist_s=[[-1]*W for _ in range(H)],[[-1]*W for _ in range(H)]
    q1,q2=deque(),deque()

    # 시작 큐 저장
    for r in range(H):
        for c in range(W):
            if graph[r][c]=='*':
                q1.append((r,c))
                dist_f[r][c]=0
            elif graph[r][c]=='@':
                q2.append((r,c))
                dist_s[r][c]=0
                
            if graph[r][c]=='#':
                dist_f[r][c]=dist_s[r][c]=0
                        
    # 불 BFS
    while q1:
        r,c=q1.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if OOB(nr,nc) or dist_f[nr][nc]>=0: continue # 이미 방문한 경우(벽 처리 포함)
            dist_f[nr][nc]=dist_f[r][c]+1
            q1.append((nr,nc))

    # 상근 BFS
    escape=False
    while q2 and not escape:
        r,c=q2.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
        
            if OOB(nr,nc): # 탈출 성공한 경우
                write(str(dist_s[r][c]+1)+"\n")
                escape=True
                break
        
            if dist_s[nr][nc]>=0: continue # 이미 방문한 경우(벽 처리 포함)
            if dist_f[nr][nc]>=0 and dist_f[nr][nc]<=dist_s[r][c]+1: continue # 불이 먼저 도착해서 도착할 수 없는 경우
            dist_s[nr][nc]=dist_s[r][c]+1
            q2.append((nr,nc))

    if not escape: write("IMPOSSIBLE\n")
