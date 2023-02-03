# https://www.acmicpc.net/problem/2003
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=list(map(int,input().strip().split()))
rt=cnt=0
tot=A[0]
for lt in range(N):
    while rt<N and tot<M:
        rt+=1
        if rt<N: tot+=A[rt]
    if rt==N: break
    if tot==M: cnt+=1
    tot-=A[lt]
    
print(cnt)