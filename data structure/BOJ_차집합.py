# https://www.acmicpc.net/problem/1822
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rst = set(A).difference(set(B))

print(len(rst))
if rst:
    print(*sorted(rst))
