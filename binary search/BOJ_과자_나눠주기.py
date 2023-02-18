# https://www.acmicpc.net/problem/16401
from sys import stdin
from bisect import bisect_left
input = stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lt, rt = 1, arr[-1]
while lt <= rt:
    mid = (lt+rt)//2
    cnt = 0
    idx = bisect_left(arr, mid)
    for i in range(idx, N):
        cnt += (arr[i]//mid)
        if cnt >= M:
            break

    if cnt >= M:
        lt = mid+1
    else:
        rt = mid-1

print(lt-1)
