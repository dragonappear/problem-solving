# https://www.acmicpc.net/problem/7569
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

M,N,H=map(int,input().split())
dr_dc_dh=[(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
dist = [[[0] * M for _ in range(N)] for _ in range(H)]
q=deque()

for a in range(H):
    for b in range(N):
        for c in range(M):
            if graph[a][b][c]==0:
                dist[a][b][c]=-1
            elif graph[a][b][c]==1:
                dist[a][b][c]=0
                q.append((a,b,c))
                
while q:
    h,r,c=q.popleft()
    for dr,dc,dh in dr_dc_dh:
        nr,nc,nh=r+dr,c+dc,h+dh
        if not(0<=nr<N) or not(0<=nc<M) or not(0<=nh<H) or dist[nh][nr][nc]>=0: continue
        dist[nh][nr][nc]=dist[h][r][c]+1 # 방문 표시
        q.append((nh,nr,nc))

mx=float('-inf')
for a in range(H):
    for b in range(N):
        for c in range(M):
            if dist[a][b][c]==-1:
                write("-1\n")
                exit()
            mx=max(mx,dist[a][b][c])
            
write(str(mx))

'''
1. 문제 읽기
2. 논리적 순서
3. 필요한 자료연산 리스트업
4. 자료형, 시간복잡도, 유리한 자료구조 선택
5. 구현
6. 엣지케이스
'''