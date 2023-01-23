# https://www.acmicpc.net/problem/2839
from sys import stdin,stdout,maxsize
input,write=stdin.readline,stdout.write

N=int(input())

# 1. 테이블 정의
# dp[N] = N 킬로그램을 구성하는 최소 봉지 개수
dp=[maxsize]*(5_001) 

# 3. 초기값 설정
dp[3]=dp[5]=1  

# 2. 점화식
# dp[N] = min(dp[N-3],dp[N-5]) + 1
for i in range(6,N+1):
    mn = min(dp[i-3],dp[i-5]) 
    if mn!=maxsize:
        dp[i]=mn+1 
        
print(dp[N] if dp[N]!=maxsize else -1)