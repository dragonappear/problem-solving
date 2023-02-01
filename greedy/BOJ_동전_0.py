# https://www.acmicpc.net/problem/11047
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,K=map(int,input().split())
COIN=[int(input()) for _ in range(N)]
COIN.reverse()
cnt=0
i=-1
while K>0 and i<N:
    i+=1
    
    if K<COIN[i]: continue
    
    n=K//COIN[i]
    K=K%COIN[i]
    
    cnt+=n

print(cnt)