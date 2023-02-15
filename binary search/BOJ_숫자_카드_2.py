# https://www.acmicpc.net/problem/10816
from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

arr.sort()
for q in query:
    lt = bisect_left(arr, q)
    if 0 <= lt < N and arr[lt] == q:
        rt = bisect_right(arr, q)
        print(rt-lt, end=' ')
    else:
        print(0, end=' ')
