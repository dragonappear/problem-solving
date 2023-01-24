# https://www.acmicpc.net/problem/2579
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
STEP=[0]*(302)
for i in range(1,N+1):
    STEP[i]=(int(input()))

# dp= N번째 계단까지 점수의 최댓값
# 별도로 단계를 지정해야함
# 전단계가 연속으로 왔는지 체크
dp= [[0]*2 for _ in range(302)]

dp[1][0]=dp[1][1]=STEP[1]
dp[2][0],dp[2][1]=STEP[2],STEP[2]+STEP[1]

for i in range(3,N+1):
    dp[i][0]=max(dp[i-2][0],dp[i-2][1])+STEP[i]
    dp[i][1]=dp[i-1][0]+STEP[i]

print(max(dp[N]))