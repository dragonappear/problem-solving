# https://www.acmicpc.net/problem/2217
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

# 최대무게는 ROPE의 배수중 하나이다.
N=int(input())
ROPE=sorted([int(input()) for _ in range(N)]) 
ans=0
for i in range(1,N+1):
    ans=max(ans,ROPE[N-i]*i)
print(ans)