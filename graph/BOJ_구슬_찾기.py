# https://www.acmicpc.net/problem/2617
from sys import stdin,stdout
from collections import defaultdict,deque
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
l_h=[[0,0] for _ in range(N+1)]
graph=defaultdict(list)
for _ in range(M):
    v,u=map(int,input().split())
    graph[u].append(v)

for start in range(1,N+1):
    visit=[False]*(N+1)
    q = deque([start])
    visit[0]=True
    while q:
        u=q.popleft()
        
        if visit[u]: continue
        
        if u!=start:
            l_h[start][1]+=1
            l_h[u][0]+=1
        
        visit[u]=True
        
        for v in graph[u]:
            if visit[v]: continue
            q.append(v)

count = 0
for i in range(1,N+1):
    if l_h[i][0]>=(N+1)//2 or l_h[i][1]>=(N+1)//2: count+=1
        
write(str(count)+"\n")