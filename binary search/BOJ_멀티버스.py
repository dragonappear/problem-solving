# https://www.acmicpc.net/problem/18869
from sys import stdin
from bisect import bisect_left
input = stdin.readline


def compress(a):
    tmp = sorted(set(a))
    for i in range(len(a)):
        a[i] = bisect_left(tmp, a[i])
    return a


def compare(a, b):
    for i in range(N):
        if a[i] != b[i]:
            return 0
    return 1


M, N = map(int, input().split())
p = [compress(list(map(int, input().split()))) for _ in range(M)]

ans = 0
for i in range(M-1):
    for j in range(i+1, M):
        ans += compare(p[i], p[j])

print(ans)
