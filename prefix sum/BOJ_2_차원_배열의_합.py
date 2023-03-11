# https://www.acmicpc.net/problem/2167
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + arr[i-1][j-1]

for _ in range(int(input())):
    sr, sc, er, ec = map(int, input().split())

    print(d[er][ec] - d[er][sc-1] - d[sr-1][ec] + d[sr-1][sc-1])
