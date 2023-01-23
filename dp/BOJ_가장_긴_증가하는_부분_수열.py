# https://www.acmicpc.net/problem/11053
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().split())) # 1 3 2 3 4 5 6 7

# 1. 테이블 정의
# dp[N] = N번째 원소까지 가장 긴 증가하는 부분 수열의 길이
dp=[1]*(N) # 3. 초기값 설정

for i in range(0,N):
    for j in range(0,i):
        if A[j]<A[i]:
            # 2. 점화식
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))
