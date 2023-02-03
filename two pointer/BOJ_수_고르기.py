# https://www.acmicpc.net/problem/2230
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=[int(input()) for _ in range(N)]
A.sort()
rt=0
mn=float('inf')
for lt in range(N):
    while rt<N and A[rt]-A[lt]<M:
        rt+=1
    if rt==N: break
    mn=min(mn,A[rt]-A[lt])
 
print(mn)