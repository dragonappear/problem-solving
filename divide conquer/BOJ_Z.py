# https://www.acmicpc.net/problem/1074
from sys import stdin
input = stdin.readline


def solve(x, y, n, cnt):

    if n == 1:
        return cnt

    half = (n >> 1)
    a = (half * half)
    half_x, half_y = x+half, y+half
    if r < half_x and c < half_y:
        return solve(x, y, half, cnt)
    elif r < half_x and c >= half_y:
        return solve(x, half_y, half, cnt+a)
    elif r >= half_x and c < half_y:
        return solve(half_x, y, half, cnt+a+a)
    else:
        return solve(half_x, half_y, half, cnt+a+a+a)


N, r, c = map(int, input().split())
print(solve(0, 0, 2**N, 0))
