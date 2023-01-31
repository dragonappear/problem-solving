# https://www.acmicpc.net/problem/1941
from sys import stdin,stdout
from itertools import combinations
from collections import deque
input,write=stdin.readline,stdout.write

def check_s(comb):
    cnt=int(sum(1 for i in range(7) if board[comb[i][0]][comb[i][1]]=='S'))
    return True if cnt>=4 else False

def check_adjacent(comb):
    visit=[False]*7
    q=deque()
    visit[0]=True
    q.append(comb[0])
    
    while q:
        r,c=q.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if (nr,nc) in comb:
                idx=comb.index((nr,nc))
                if not visit[idx]:
                    q.append((nr,nc))
                    visit[idx]=True
                    
    return False if False in visit else True
    
board=[list(input().strip()) for _ in range(5)]
pos=[(i,j) for i in range(5) for j in range(5)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
ans=0
for comb in list(combinations(pos,7)):
    if check_s(comb) and check_adjacent(comb):
        ans+=1
print(ans)