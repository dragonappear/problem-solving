# https://www.acmicpc.net/problem/1463
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

dp=[0] * (10**6+1)
dp[1],dp[2],dp[3]=0,1,1

N=int(input())
for i in range(4,N+1):
    cd=[]
    if i%3==0:
        cd.append(dp[i//3])
    if i%2==0:
        cd.append(dp[i//2])
    cd.append(dp[i-1])
    
    dp[i]=min(cd)+1

print(dp[N])