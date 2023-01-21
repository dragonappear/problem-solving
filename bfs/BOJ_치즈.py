# https://www.acmicpc.net/problem/2638
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

"""
1. 0에 대해서 BFS 순회(0만 순회하기 위해 0만 큐에 삽입)
2. 0에서 1로 순회시 큐에 넣지않고 1에 방문횟수 추가
3. 0 방문 모두 끝나면 치즈 지우기 + 남은 치즈는 원복
4. 치즈가 사라질때까지 반복

time: O(NM) n,m=[1,100]
space: O(NM) n,m=[1,100]
"""

def bfs():
    visit = [[False] * M for _ in range(N)]
    q = deque([(0,0)])
    visit[0][0]=True
    while q:
        r,c= q.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not (0<=nr<N) or not (0<=nc<M) or visit[nr][nc]: continue
            if graph[nr][nc]==0:
                visit[nr][nc]=True
                q.append((nr,nc))
            else:
                graph[nr][nc]+=1

N,M=map(int,input().split())
graph=[ list(map(int,input().strip().split())) for _ in range(N)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
cheeze_count=sum( graph[i].count(1) for i in range(N))
time = 0
while True:
    if cheeze_count<=0: break
    
    bfs()
    for i in range(N):
        for j in range(M):
            if graph[i][j]>=3:
                graph[i][j]=0
                cheeze_count-=1
            elif graph[i][j]==2:
                graph[i][j]=1
    time+=1
    
write(str(time)+"\n")