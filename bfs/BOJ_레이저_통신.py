# https://www.acmicpc.net/problem/6087
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

"""
BFS를 활용한 최단거리 문제
거리를 묻는거같지만, 종료점까지 최소 거울을 사용하여 도달하면 되는 문제
각 정점에 최소 거울로 갈 수 있는 그래프를 그리기

time:O(W^2+H^2) W,H=[1,10^2]
space:O(WH)
"""

W,H=map(int,input().split())
graph=list(list(input().strip()) for _ in range(H))
mirrors = [[float('inf')] * W for _ in range(H)]
c=[(i,j) for j in range(W) for i in range(H) if graph[i][j]=='C']
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
(start_r,start_c),(end_r,end_c)=c[0],c[1]

mirrors[start_r][start_c]=0
q = deque([(start_r,start_c,0)])
while q:
    r,c,m=q.popleft()
    
    if r==end_r and c==end_c:
        write(str(mirrors[r][c]))
        break
    
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        while True:
            if not (0<=nr<H) or not (0<=nc<W) or graph[nr][nc]=="*" or (mirrors[nr][nc] < m):
                break
            mirrors[nr][nc]=m
            q.append((nr,nc,m+1))
            nr,nc=nr+dr,nc+dc