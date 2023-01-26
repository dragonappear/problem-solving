# https://www.acmicpc.net/problem/10844
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

MOD=1000000000
N=int(input())

# 테이블 정의
# d[i][j] = 길이가 i번째 숫자 j의 개수
d= [[0]*10 for _ in range(102)] # d[102][10]

for i in range(1,10):
    d[1][i]=1

for i in range(2,N+1):
    for k in range(10):
        if k!=0: d[i][k]+=d[i-1][k-1]
        if k!=9: d[i][k]+=d[i-1][k+1]
        d[i][k] %= MOD

ans=0
for i in range(10):
    ans += d[N][i]
    ans %= MOD

print(ans)