# https://www.acmicpc.net/problem/15651
from sys import stdin,stdout
from itertools import product
input,write=stdin.readline,stdout.write

def dfs(arr):
    
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(1,N+1):
        dfs(arr+[i])


N,M=map(int,input().split())

# 풀이1
dfs([])

# 풀이2
for p in list(product([i for i in range(1,N+1)],repeat=M)):
    print(*p)