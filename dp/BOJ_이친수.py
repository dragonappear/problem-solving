# https://www.acmicpc.net/problem/2193
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
DP=[[0]* 2 for _ in range(92)]
# [N][0] 은 0 삽입
# [N][1] 은 1 삽입
DP[1][0],DP[1][1]=0,1

for i in range(2,N+1):
    DP[i][0]=DP[i-1][0]+DP[i-1][1]
    DP[i][1]=DP[i-1][0]
    
print(sum(DP[N]))