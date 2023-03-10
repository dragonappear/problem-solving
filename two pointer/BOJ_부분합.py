# https://www.acmicpc.net/problem/1806
from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = float('inf')
sm = rt = 0
for lt in range(N-1):
    while rt < N and sm+arr[rt] < S:
        sm += arr[rt]
        rt += 1

    if rt == N:
        break

    ans = min(ans, rt-lt+1)
    sm -= arr[lt]

print(ans if ans != float('inf') else 0)
