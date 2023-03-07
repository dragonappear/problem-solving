# https://www.acmicpc.net/problem/2293
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

d = [0]*(100_001)
d[0] = 1

for i in range(N):
    for j in range(arr[i], K+1):
        d[j] += d[j-arr[i]]

print(d[K])
