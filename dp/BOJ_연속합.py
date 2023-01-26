# https://www.acmicpc.net/problem/1912
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().strip().split()))
dp=[0]*(N)
dp[0]=A[0]
for i in range(1,N):
    if A[i]+dp[i-1]<A[i]:
        dp[i]=A[i]
    else:
        dp[i]=A[i]+dp[i-1]

print(max(dp))