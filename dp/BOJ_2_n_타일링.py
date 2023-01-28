# https://www.acmicpc.net/problem/11726
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
MOD=10_007
d=[0]*(1_010)
d[1],d[2]=1,2

for i in range(3,N+1):
    d[i]= (d[i-1]+d[i-2])%MOD

print(d[N])