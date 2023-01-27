# https://www.acmicpc.net/problem/15649
from sys import stdin,stdout
from itertools import permutations
input,write=stdin.readline,stdout.write

def dfs(arr):
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(1,N+1):
        if visited[i]: continue
        visited[i]=True
        dfs(arr+[i])
        visited[i]=False

N,M=map(int,input().split())
visited=[False]*(N+1)

# 풀이1
dfs([])

# 풀이2
for a in list(permutations([i for i in range(1,N+1)],M)):
    print(*a)