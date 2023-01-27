# https://www.acmicpc.net/problem/15655
from sys import stdin,stdout
from itertools import permutations
input,write=stdin.readline,stdout.write

def dfs(idx,arr):
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(idx,N):
        if visit[i]: continue
        visit[i]=True
        dfs(i,arr+[A[i]])
        visit[i]=False

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort() # 오름차순
visit=[False]*N

# 풀이1
dfs(0,[])

#풀이2
for p in permutations(A,r=M):
    if sorted(p)==list(p): 
        print(*p)