# https://www.acmicpc.net/problem/8980
from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
M = int(input())

arr = [list(map(int, input().split())) for _ in range(M)]
arr.sort(key=lambda x: (x[1]))

ans = 0
box = [C] * (N+1)
for st, en, weight in arr:

    mn = float('inf')

    for i in range(st, en):
        mn = min(mn, box[i])

    mn = min(mn, weight)

    for i in range(st, en):
        box[i] -= mn

    ans += mn

print(ans)
