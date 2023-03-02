# https://www.acmicpc.net/problem/12015
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
d = [arr[0]]  # d[i]: 길이가 i인 최장부분수열의 값

for i in range(1, N):
    n = arr[i]

    if n > d[-1]:
        d.append(n)
    else:
        idx = bisect_left(d, n)
        if 0 <= idx < len(d):
            d[idx] = n

print(len(d))
