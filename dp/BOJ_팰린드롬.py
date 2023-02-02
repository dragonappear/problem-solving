# https://www.acmicpc.net/problem/10942
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input()) # [1,2000]
A=[0]+list(map(int,input().strip().split()))

# 양끝이 같으면, 양끝제외 중앙부분이 펠린드롬이면 팰린드롬이다.
# d[i][j]: i~j까지 팰린드롬인지 아닌지
d=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    d[i][i]=1 # 5 => 팰린드롬
    if A[i-1]==A[i]: d[i-1][i]=1 # ex) 1005 1005 => 팰린드롬
    
for gap in range(2,N):
    for i in range(1,N-gap+1):
        s,e=i,i+gap
        if A[s]==A[e] and d[s+1][e-1]==1: # 가운데가 팰린드롬이고 양끝이 같으면 팰린드롬
            d[s][e]=1

for _ in range(int(input())): # [1,1_000_000]
    S,E=map(int,input().strip().split())
    print(d[S][E])