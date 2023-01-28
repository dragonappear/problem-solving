# https://www.acmicpc.net/problem/15665
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def dfs(arr):
    if len(arr)==M:
        print(*arr)
        return
    
    tmp=-1
    for i in range(N):
        if tmp==A[i]: continue
        tmp=A[i]
        dfs(arr+[A[i]])
    
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
dfs([])