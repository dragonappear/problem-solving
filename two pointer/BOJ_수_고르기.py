# https://www.acmicpc.net/problem/2230
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

ans = float('inf')
rt = 0
for lt in range(N):
    while rt < N and arr[rt] - arr[lt] < M:
        rt += 1

    if rt == N:
        break

    ans = min(ans, arr[rt] - arr[lt])

print(ans)
