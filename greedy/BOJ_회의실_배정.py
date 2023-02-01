# https://www.acmicpc.net/problem/1931
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
C=[[0,0] for _ in range(N)]
for i in range(N):
    C[i][0],C[i][1]=map(int,input().split())
C.sort(key=lambda x:(x[1],x[0]))

cnt=0
prev=0
for i in range(N):
    if C[i][0]>=prev:
        cnt+=1
        prev=C[i][1]
    else: continue

print(cnt)