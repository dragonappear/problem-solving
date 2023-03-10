# https://www.acmicpc.net/problem/8980
from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
M = int(input())

arr = [list(map(int, input().split())) for _ in range(M)]

# 빨리 실고 내리는게 이득이므로 도착지 순으로 정렬한다.
arr.sort(key=lambda x: (x[1]))

ans = 0
capacity = [C] * (N+1)  # 잔여용량
for st, en, weight in arr:

    mn = weight
    for i in range(st, en):
        mn = min(mn, capacity[i])

    for i in range(st, en):
        capacity[i] -= mn

    ans += mn

print(ans)
