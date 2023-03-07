# https://www.acmicpc.net/problem/2294
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

d = [float('inf')] * 100_001
d[0] = 0

for i in range(N):
    for j in range(arr[i], K+1):
        d[j] = min(d[j], d[j-arr[i]]+1)

print(d)
print(d[K] if d[K] != float('inf') else -1)
