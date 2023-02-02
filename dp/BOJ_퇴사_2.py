# https://www.acmicpc.net/problem/15486
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
T=[0]*(1_500_002)
P=[0]*(1_500_002)
d=[0]*(1_500_002)

for i in range(1,N+1):
    T[i],P[i]=map(int,input().split())

for i in range(N,0,-1):
    if i+T[i]<=N+1:
        d[i]=max(d[i+1],d[i+T[i]]+P[i])
    else:
        d[i]=d[i+1]

print(d[1])