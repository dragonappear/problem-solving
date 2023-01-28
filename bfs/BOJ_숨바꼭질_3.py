# https://www.acmicpc.net/problem/13549
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def teleport(i):
    tmp=i
    if not tmp: return
    while tmp<MX and dist[K]==0:
        if dist[tmp]==0:
            dist[tmp]=dist[i]
            q.append(tmp)
            if tmp==K: return
        tmp<<=1
        
MX=100_010
N,K=map(int,input().split())
dist=[0]*MX
dist[N]=1

q=deque([N])
teleport(N)

while q:
    u=q.popleft()
    for n in [u-1,u+1]:
        if not(0<=n<MX) or dist[n]: continue
        dist[n]=dist[u]+1
        q.append(n)
        teleport(n)
print(dist[K]-1)