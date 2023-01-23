# https://www.acmicpc.net/problem/1003
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def fibo(n:int):
    if n==0:
        return dp[0]
    elif n==1:
        return dp[1]
    else:
        if dp[n]!=[0,0]: return dp[n]
        n1=fibo(n-1)
        n2=fibo(n-2)
        
        # 2. 점화식
        # dp[n] = dp[n-1]+dp[n-2]
        dp[n]=[n1[0]+n2[0],n1[1]+n2[1]]
        return dp[n]

# 1.테이블 정의
# dp[N] = N번째 피보나치 수에 등장하는 0과 1의 개수
dp = [[0,0]] * (41) 

# 3. 초기값 설정
dp[0],dp[1]=[1,0],[0,1]

for _ in range(int(input())):
    N=int(input())
    fibo(N)
    print(dp[N][0],dp[N][1])