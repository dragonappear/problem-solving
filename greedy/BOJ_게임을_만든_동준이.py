# https://www.acmicpc.net/problem/2847
from sys import stdin
input = stdin.readline

N = int(input())
score = [int(input()) for _ in range(N)]

ans = 0
mx = score[-1]

for i in range(N-2, -1, -1):
    if mx <= score[i]:
        diff = abs(score[i]-mx)+1
        ans += diff
        score[i] -= diff
    mx = score[i]


print(ans)
