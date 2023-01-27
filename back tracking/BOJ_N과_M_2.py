# https://www.acmicpc.net/problem/15650
from sys import stdin,stdout
from itertools import permutations
input,write=stdin.readline,stdout.write

def dfs(index,arr):
    
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(index,N+1):
        if visit[i]: continue
        visit[i]=True
        dfs(i,arr+[i])
        visit[i]=False

N,M=map(int,input().split())
visit=[False]*(N+1)

# 풀이1
dfs(1,[])

# 풀이2
for p in list(permutations([i for i in range(1,N+1)],M)):
    if len(p)==1: print(*p)
    else:
        perm=list(p)
        if sorted(perm)==perm:
            print(*perm)