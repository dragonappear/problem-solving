# https://www.acmicpc.net/problem/1699
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
d=[0]*(100_002)

for i in range(1,N+1):
    d[i]=i
    j=1
    while j*j<=i:
        d[i]=min(d[i],d[i-j*j]+1)
        j+=1

print(d[N])