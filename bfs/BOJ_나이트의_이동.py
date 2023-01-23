# https://www.acmicpc.net/problem/7562
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def bfs():
    visit = [[False] * I for _ in range(I)] 
    visit[sr][sc]=True
    q=deque([(sr,sc,0)])
    while q:
        r,c,d=q.popleft()
        if r==er and c==ec:
            return d
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not(0<=nr<I) or not(0<=nc<I) or visit[nr][nc]: continue
            visit[nr][nc]=True
            q.append((nr,nc,d+1))

for _ in range(int(input())):
    I=int(input())
    sr,sc=map(int,input().strip().split())
    er,ec=map(int,input().strip().split())
    dr_dc=[(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
    if sr==er and sc==ec:
        write("0\n")
        continue
    write(str(bfs())+"\n")