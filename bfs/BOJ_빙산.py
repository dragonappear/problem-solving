# https://www.acmicpc.net/problem/2573
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def melting():
    zero = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]==0: continue
            for dr,dc in dr_dc:
                nr,nc=i+dr,j+dc
                if (0<=nr<N) and (0<=nc<M) and board[nr][nc]==0:
                    zero[i][j]+=1
    for i in range(N):
        for j in range(M):
            board[i][j]=max(0,board[i][j]-zero[i][j])
                        
def bfs():
    x,y=-1,-1
    cnt1=0 # 빙산의 개수
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                x,y=i,j
                cnt1+=1
    if cnt1==0: return 0
    
    cnt2=0 # (x,y)와 붙어있는 빙산의 개수
    q=deque([(x,y)])
    visit[x][y]=True
    while q:
        r,c=q.popleft()
        cnt2+=1
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not(0<=nr<N) or not(0<=nc<M) or visit[nr][nc] or board[nr][nc]==0: continue
            visit[nr][nc]=True
            q.append((nr,nc))
            
    if cnt1==cnt2: return 1 # 한덩이
    return 2 # 2덩이이상
            
N,M=map(int,input().split())
board=[list(map(int,input().strip().split())) for _ in range(N)]
dr_dc=[(1,0), (0,1), (-1,0), (0,-1)]

time=0
while True:
    time+=1
    melting()
    visit = [[False] * M for _ in range(N)]
    rst=bfs()
    if rst==0:
        write("0\n")
        exit()
    elif rst==1: continue
    else: break

write(str(time)+"\n")
