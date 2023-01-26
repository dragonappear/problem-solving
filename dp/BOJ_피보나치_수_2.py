# https://www.acmicpc.net/problem/2748
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
d=[0]*100
d[1]=d[2]=1

for i in range(3,N+1):
    d[i]=d[i-2]+d[i-1]

print(d[N])