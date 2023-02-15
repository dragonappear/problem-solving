# https://www.acmicpc.net/problem/2295
from sys import stdin
from itertools import combinations_with_replacement
input = stdin.readline

N = int(input())
arr = list(set([int(input().strip()) for _ in range(N)]))
arr.sort(reverse=True)
s = set(arr)
mx = 0
for a, b, c in combinations_with_replacement(arr, r=3):
    if (a+b+c) in s:
        mx = max(mx, (a+b+c))
        break
print(mx)
