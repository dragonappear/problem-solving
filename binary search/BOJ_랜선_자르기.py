# https://www.acmicpc.net/problem/1654
from sys import stdin
input = stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
arr.sort()

lt, rt = 1, arr[-1]

while lt <= rt:
    mid = lt + (rt-lt)//2

    cnt = 0
    for a in arr:
        cnt += (a//mid)

    if cnt >= N:
        lt = mid+1
    else:
        rt = mid-1

print(lt-1)
