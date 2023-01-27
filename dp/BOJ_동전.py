# https://www.acmicpc.net/problem/9084
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

for _ in range(int(input())):
    N=int(input().strip())
    A= list(map(int,input().strip().split()))
    M=int(input().strip())
    
    d=[0]*(10_010)
    d[0]=1
    for i in range(N):
        for j in range(A[i],M+1):
            d[j]+=d[j-A[i]]
    print(d[M])