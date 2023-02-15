# https://www.acmicpc.net/problem/2295
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(set([int(input().strip()) for _ in range(N)]))
two = []
arr.sort()

for i in range(len(arr)):
    for j in range(i, len(arr)):
        two.append(arr[i]+arr[j])

two.sort()

for i in range(N-1, -1, -1):
    for j in range(0, i):
        target = arr[i]-arr[j]
        idx = bisect_left(two, target)
        if 0 <= idx < len(two) and two[idx] == target:
            print(arr[i])
            exit()
