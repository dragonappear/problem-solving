# https://www.acmicpc.net/problem/11047
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

ans = 0
idx = N-1
while K:

    if arr[idx] > K:
        idx -= 1
        continue
    else:
        a = (K//arr[idx])
        K -= a*arr[idx]
        ans += a

print(ans)
