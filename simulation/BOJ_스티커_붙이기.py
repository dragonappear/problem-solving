# https://www.acmicpc.net/problem/18808
from sys import stdin
input = stdin.readline


def possible(i, j, idx):
    arr, n, m = stickers[idx]

    if i+n > N or j+m > M:
        return False

    for r in range(n):
        for c in range(m):
            x = (i+r)
            y = (j+c)
            if board[x][y] and arr[r][c]:
                return False

    for r in range(n):
        for c in range(m):
            if arr[r][c]:
                x = (i+r)
                y = (j+c)
                board[x][y] = arr[r][c]

    return True


def rotate(idx):
    arr, n, m = stickers[idx]
    tmp = [[0] * 12 for _ in range(12)]

    for i in range(m):
        for j in range(n):
            tmp[i][j] = arr[n-1-j][i]

    stickers[idx] = [tmp, m, n]


N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
stickers = []

for _ in range(K):
    r, c = map(int, input().split())
    tmp = [[0] * 12 for _ in range(12)]
    for i in range(r):
        arr = list(map(int, input().split()))
        for j in range(c):
            tmp[i][j] = arr[j]
    stickers.append([tmp, r, c])


for k in range(K):
    for _ in range(4):
        escape = False
        for i in range(N):
            for j in range(M):
                if possible(i, j, k):
                    escape = True
                    break
            if escape:
                break
        if escape:
            break

        rotate(k)

print(int(sum(1 for i in range(N) for j in range(M) if board[i][j])))
