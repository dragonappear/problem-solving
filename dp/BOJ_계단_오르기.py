# https://www.acmicpc.net/problem/2579
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
S=[0]+[int(input()) for _ in range(N)]
d=[[0]*(3) for _ in range(N+1)]

# dp[i][j]= 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을때 점수 합의 최댓값(단,i번째 계단은 반드시 밟아야함)
d[1][1]=d[1][2]=S[1]

for i in range(2,N+1):
    d[i][1]= max( d[i-2][1], d[i-2][2] )+S[i]
    d[i][2]=d[i-1][1]+S[i]
    
print(max(d[N]))