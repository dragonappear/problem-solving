# https://www.acmicpc.net/problem/2167
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

psum = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        psum[i][j] = (psum[i-1][j] + psum[i][j-1] -
                      psum[i-1][j-1]) + arr[i-1][j-1]

for _ in range(int(input())):
    sr, sc, er, ec = map(int, input().split())

    print(psum[er][ec] - psum[er][sc-1] - psum[sr-1][ec] + psum[sr-1][sc-1])
