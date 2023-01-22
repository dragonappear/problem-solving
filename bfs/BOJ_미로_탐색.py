# https://www.acmicpc.net/problem/2178
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
graph=[ list(map(int,input().strip())) for _ in range(N)]
q=deque([(0,0)])
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
graph[0][0]+=1

while q:
    r,c=q.popleft()
    
    if r==N-1 and c==M-1:
        write(str(graph[r][c]-1)+"\n")
        break
        
    for dr,dc in dr_dc:
        nr,nc=r+dr,c+dc
        if not(0<=nr<N) or not(0<=nc<M) or not(graph[nr][nc]) or graph[nr][nc]!=1: continue
        graph[nr][nc]=graph[r][c]+1
        q.append((nr,nc))