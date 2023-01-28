# https://www.acmicpc.net/problem/12852
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
d=[0]*(1_000_010)
prev=[0]*(1_000_010)
d[1],d[2],d[3]=0,1,1
prev[1],prev[2],prev[3]=0,1,1
for i in range(4,N+1):
    d[i]=d[i-1]+1
    prev[i]=i-1
    if i%2==0:
        if d[i]>d[i//2]+1:
            d[i]=d[i//2]+1
            prev[i]=i//2
    if i%3==0:
        if d[i]>d[i//3]+1:
            d[i]=d[i//3]+1
            prev[i]=i//3

print(d[N])
t=N
while t:
    print(t,end=' ')
    t=prev[t]