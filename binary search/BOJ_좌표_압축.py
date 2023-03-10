# https://www.acmicpc.net/problem/18870
from sys import stdin
from bisect import bisect_left
input = stdin.readline


def compress():
    tmp = sorted(set(arr))
    for i in range(N):
        arr[i] = bisect_left(tmp, arr[i])


N = int(input())
arr = list(map(int, input().split()))
compress()
print(*arr)
