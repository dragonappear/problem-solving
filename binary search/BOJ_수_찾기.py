# https://www.acmicpc.net/problem/1920
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

arr.sort()

for q in query:
    idx = bisect_left(arr, q)
    if 0 <= idx < N and arr[idx] == q:
        print(1)
    else:
        print(0)
