# https://www.acmicpc.net/problem/18222
from sys import stdin
input = stdin.readline


def solve(n):
    if n == 1:
        return 0

    i = 1
    while (i << 1) < n:
        i <<= 1

    return (solve(n-i)+1) % 2


N = int(input())
print(solve(N))
