# https://www.acmicpc.net/problem/18870
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
tmp = sorted(set(arr))
for a in arr:
    idx = bisect_left(tmp, a)
    print(idx, end=' ')
