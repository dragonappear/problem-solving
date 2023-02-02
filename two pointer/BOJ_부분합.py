# https://www.acmicpc.net/problem/1806
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,S=map(int,input().strip().split())
A=list(map(int,input().strip().split()))

rt=0
total=A[0]
mn=float('inf')
for lt in range(N):
    while rt<N and total<S:
        rt+=1
        if rt!=N: total+=A[rt]
    
    if rt==N: break
    mn=min(mn,rt-lt+1) 
    total-=A[lt]
    
print(mn if mn!=float('inf') else 0)