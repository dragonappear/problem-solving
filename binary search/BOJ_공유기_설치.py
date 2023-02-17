# https://www.acmicpc.net/problem/2110
from sys import stdin
from bisect import bisect_left
input = stdin.readline


def solve(len):
    idx = cnt = 0
    while idx != N:
        idx = bisect_left(arr, arr[idx]+len, idx, N)
        cnt += 1
    return cnt >= C


N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

lt, rt = 1, 1_000_000_000

while lt < rt:
    mid = (lt+rt+1)//2
    if solve(mid):
        lt = mid
    else:
        rt = mid-1

print(lt)
