# https://www.acmicpc.net/problem/11659
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=list(map(int,input().strip().split()))
dp = [0] * (N+2)

dp[1]=A[0]
for i in range(2,N+1):
    dp[i]=dp[i-1]+A[i-1]

for _ in range(M):
    i,j=map(int,input().strip().split())
    print(dp[j]-dp[i-1])