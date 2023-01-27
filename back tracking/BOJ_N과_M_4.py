# https://www.acmicpc.net/problem/15652
from sys import stdin,stdout
from itertools import product
input,write=stdin.readline,stdout.write

def dfs(idx,arr):
    
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(idx,N+1):
        dfs(i,arr+[i])

N,M=map(int,input().split())

# 풀이1
dfs(1,[])

# 풀이2
# 시간초과
for p in product([i for i in range(1,N+1)],repeat=M):
    if len(p)==1: 
        print(*p)
    else:
        escape=False
        for i in range(1,len(p)):
            if p[i-1]>p[i]:
                escape=True
                break
        if not escape: print(*p)