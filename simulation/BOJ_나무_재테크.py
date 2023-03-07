# https://www.acmicpc.net/problem/16235
from sys import stdin
input = stdin.readline


def spring_summer():
    for i in range(N):
        for j in range(N):
            if tree[i][j] == []:
                continue

            tree[i][j].sort()

            idx = -1
            num = len(tree[i][j])
            for k in range(num):
                if field[i][j] >= tree[i][j][k]:
                    field[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    idx = k
                    break

            if idx != -1:
                for k in range(idx, num):
                    field[i][j] += (tree[i][j][k]//2)

                for k in range(idx, num):
                    tree[i][j].pop()


def fall_winter():

    for r in range(N):
        for c in range(N):
            if tree[r][c] == []:
                continue

            for k in range(len(tree[r][c])):
                if tree[r][c][k] % 5 == 0:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                        nr, nc = r+dr, c+dc
                        if not(0 <= nr < N) or not(0 <= nc < N):
                            continue
                        tree[nr][nc].append(1)

    for i in range(N):
        for j in range(N):
            field[i][j] += plus[i][j]


N, M, K = map(int, input().split())
field = [[5]*N for _ in range(N)]
plus = [list(map(int, input().split())) for _ in range(N)]
tree = [[list() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, a = map(int, input().split())
    tree[x-1][y-1].append(a)

for _ in range(K):
    spring_summer()
    fall_winter()

print(int(sum(len(tree[i][j]) for i in range(N) for j in range(N))))
