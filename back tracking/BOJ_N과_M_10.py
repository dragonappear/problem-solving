# https://www.acmicpc.net/problem/15664
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def dfs(start,arr):
    if len(arr)==M:
        print(*arr)
        return
    
    tmp=-1
    for i in range(start,N):
        if visit[i] or tmp==A[i]: continue
        visit[i]=True
        tmp=A[i]
        dfs(i,arr+[A[i]])
        visit[i]=False
    
N,M=map(int,input().split())
A=list(map(int,input().split()))
visit=[False]*N
A.sort()

# 풀이1
dfs(0,[])