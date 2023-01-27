# https://www.acmicpc.net/problem/15654
from sys import stdin,stdout
from itertools import permutations
input,write=stdin.readline,stdout.write

def dfs(arr):
    
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(N):
        if visit[i]: continue
        visit[i]=True
        dfs(arr+[A[i]])
        visit[i]=False


N,M=map(int,input().split())
A=list(map(int,input().strip().split())) # 모두 다른 수
A.sort() # 사전순 출력
visit=[False]*N

# 풀이 1
dfs([])

# 풀이2
for p in permutations(A,r=M):
    print(*p)