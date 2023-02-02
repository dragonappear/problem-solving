# https://www.acmicpc.net/problem/2559
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,K=map(int,input().split())
T=list(map(int,input().strip().split()))

s=sum(T[0:K])
mx=s
for lt in range(1,N-K+1):    
    s=s-T[lt-1]+T[lt+K-1]
    mx=max(mx,s)
    
print(mx)