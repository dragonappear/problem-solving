# https://www.acmicpc.net/problem/11727
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
dp=[0]*(1_001)
dp[1],dp[2],dp[3]=1,3,5

for i in range(4,N+1):
    dp[i]= (dp[i-1]+2*dp[i-2])%10_007

print(dp[N])