# https://www.acmicpc.net/problem/1932
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=[list(map(int,input().strip().split())) for _ in range(N)];

# 1. 테이블
# dp = 2차원 배열
# dp[i][j] = i행 j열까지 수의 최대 합 경로
# 3. 초기값
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        # 2. 점화식
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + A[i-1][j-1]

print(max(dp[N]))