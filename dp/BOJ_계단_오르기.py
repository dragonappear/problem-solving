# https://www.acmicpc.net/problem/2579
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
STEP=[0]*(302)
for i in range(1,N+1):
    STEP[i]=(int(input()))

# dp[i][j]= 현재까지 j개의 계단을 연속해서 밝고 i번째 계단까지 올라섰을때 점수 합의 최댓값(단,i번째 계단은 반드시 밟아야함)
dp= [[0]*2 for _ in range(302)]

dp[1][0]=dp[1][1]=STEP[1]
dp[2][0],dp[2][1]=STEP[2],STEP[2]+STEP[1]

for i in range(3,N+1):
    dp[i][0]=max(dp[i-2][0],dp[i-2][1])+STEP[i]
    dp[i][1]=dp[i-1][0]+STEP[i]

print(max(dp[N]))