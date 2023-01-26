# https://www.acmicpc.net/problem/11055
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().strip().split()))
d=[0]*(N)
d[0]=A[0]

for i in range(1,N):
    mx=-1
    for j in range(i):
        if A[j]<A[i]:
            mx = max(mx,d[j])
    if mx!=-1: d[i]=mx+A[i]
    else: d[i]=A[i]

print(max(d))