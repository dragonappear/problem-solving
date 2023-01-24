# https://www.acmicpc.net/problem/9095
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

dp = [0] * 12
dp[1],dp[2],dp[3]=1,2,4

for i in range(4,12):
    dp[i]= dp[i-3]+dp[i-2]+dp[i-1]

for _ in range(int(input())):
    N=int(input().strip())
    write(str(dp[N])+"\n")