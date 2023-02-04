# https://www.acmicpc.net/problem/1946
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

for _ in range(int(input())):
    N=int(input())
    A=[[0,0] for _ in range(N+1)]
    for i in range(N):
        doc,itv=map(int,input().split())
        A[doc]=itv
        
    cnt=N
    tmp=A[1]
    for i in range(2,N+1):
        
        if tmp<A[i]:
            cnt-=1
        else:
            tmp=A[i]
    print(cnt)
    