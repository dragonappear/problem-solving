# https://www.acmicpc.net/problem/11725
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def rotate(R, C):

    tmp = [[0]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            tmp[r][c] = sticker[r][c]

    # 회전
    for r in range(C):
        for c in range(R):
            sticker[r][c] = tmp[R-c-1][r]

    return C, R


def possible(r, c):
    for i in range(R):
        for j in range(C):
            if board[i+r][j+c] == 1 and sticker[i][j] == 1:
                return False

    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                board[i+r][j+c] = 1

    return True


N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())

    # 회전위해 넉넉히
    sticker = [[0]*12 for _ in range(12)]

    # 입력
    for i in range(R):
        arr = list(map(int, input().split()))
        for j in range(C):
            sticker[i][j] = arr[j]

    for _ in range(4):
        attached = False
        for r in range(N-R+1):
            if attached:
                break

            for c in range(M-C+1):
                if possible(r, c):
                    attached = True
                    break

        if attached:
            break

        R, C = rotate(R, C)

print(int(sum(1 for i in range(N) for j in range(M) if board[i][j] == 1)))
