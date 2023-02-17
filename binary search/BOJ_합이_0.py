# https://www.acmicpc.net/problem/3151
from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = set(arr)
rst = 0
for i in range(N-1):
    for j in range(i+1, N):
        target = -(arr[i]+arr[j])
        if target in s:
            cnt = bisect_right(arr, target, j+1, N) - \
                bisect_left(arr, target, j+1, N)
            rst += cnt

print(rst)
