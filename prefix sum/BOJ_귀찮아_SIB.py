# https://www.acmicpc.net/problem/14929
from sys import stdin
input = stdin.readline

N = int(input())
X = list(map(int, input().split()))
psum = [0]*(N+1)


for i in range(1, N+1):
    psum[i] = psum[i-1]+X[i-1]

ans = 0
for i in range(1, N):
    ans += (psum[i]*X[i])

print(ans)
