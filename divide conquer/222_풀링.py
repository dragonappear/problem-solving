# https://www.acmicpc.net/problem/17829
from sys import stdin
input = stdin.readline


def solve(i, j, n):
    if n == 1:
        return board[i][j]

    half = (n >> 1)

    rst = []
    rst.append(solve(i, j, half))
    rst.append(solve(i+half, j, half))
    rst.append(solve(i, j+half, half))
    rst.append(solve(i+half, j+half, half))
    rst.sort()

    return rst[-2]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solve(0, 0, N))
