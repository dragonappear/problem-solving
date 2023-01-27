# https://www.acmicpc.net/problem/15656
from sys import stdin,stdout
from itertools import product
input,write=stdin.readline,stdout.write

def dfs(arr):
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(N):
        dfs(arr+[A[i]])
        

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort() # 오름차순 출력

# 풀이1
dfs([])

# 풀이2
for p in product(A,repeat=M):
    print(*p)