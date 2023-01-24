# https://www.acmicpc.net/problem/1149
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
RGB= [[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    RGB[i][0],RGB[i][1],RGB[i][2]=map(int,input().split())

dp=[[0]*3 for _ in range(N+1)]

dp[1][0],dp[1][1],dp[1][2]=RGB[1][0],RGB[1][1],RGB[1][2]

for i in range(2,N+1):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+RGB[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+RGB[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+RGB[i][2]

print(min(dp[N]))