# https://www.acmicpc.net/problem/14938
from sys import stdin
input = stdin.readline
INF = float('inf')

N, M = map(int, input().split())
d = [[INF] * N for _ in range(N)]  # i에서 j까지 가는데 바꿔야하는 양방향의 개수

for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = 0  # 길이 있고 지날 수 있는 방향은 0
    d[b-1][a-1] = 0 if c else 1  # 길은 있지만 지날수 없는 방향은 1

for i in range(N):
    d[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(d[a-1][b-1])
