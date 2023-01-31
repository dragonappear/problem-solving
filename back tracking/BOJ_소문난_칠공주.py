# https://www.acmicpc.net/problem/1941
from sys import stdin,stdout
from itertools import combinations
from collections import deque
input,write=stdin.readline,stdout.write

def check_s(comb):
    cnt=int(sum(1 for i in range(7) if board[comb[i][0]][comb[i][1]]=='S'))
    return True if cnt>=4 else False

def check_adjacent(arr):
    visit=[False]*7
    q=deque()
    visit[0]=True
    q.append(arr[0])
    
    while q:
        r,c=q.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if (nr,nc) in arr:
                idx=arr.index((nr,nc))
                if not visit[idx]:
                    q.append((nr,nc))
                    visit[idx]=True
                    
    return False if False in visit else True

def dfs(start,arr):
    global ans
    
    if len(arr)==7:
        if check_s(arr) and check_adjacent(arr):
            ans+=1
        return
    
    for i in range(start,25):
        if visit[i]: continue
        visit[i]=True
        dfs(i+1,arr+[(i//5,i%5)])
        visit[i]=False

board=[list(input().strip()) for _ in range(5)]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
visit=[False]*25
ans=0

# 풀이1
dfs(0,[])

# 풀이2
pos=[(i,j) for i in range(5) for j in range(5)]
for comb in list(combinations(pos,7)):
    if check_s(comb) and check_adjacent(comb):
        ans+=1

print(ans)