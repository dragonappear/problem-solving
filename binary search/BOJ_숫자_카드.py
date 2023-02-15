# https://www.acmicpc.net/problem/10815
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
C = list(map(int, input().strip().split()))
M = int(input())
query = list(map(int, input().strip().split()))

C.sort()

for q in query:
    idx = bisect_left(C, q)
    if 0 <= idx < N and C[idx] == q:
        print(1, end=' ')
    else:
        print(0, end=' ')
