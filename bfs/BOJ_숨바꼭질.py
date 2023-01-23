# https://www.acmicpc.net/problem/1697
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

N,K=map(int,input().split())
visit=[False]*(100_001)
visit[N]=True
q=deque([(N,0)])
while q:
    x,t=q.popleft()
    
    if x==K:
        write(str(t)+"\n")
        break
    
    for nx in [x-1,x+1,2*x]:
        if not(0<=nx<100_001) or visit[nx]: continue
        visit[nx]=True
        q.append((nx,t+1))