# https://www.acmicpc.net/problem/18808
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

# 회전하는 함수


def rotate(A, B):
    tmp = [[0]*12 for _ in range(12)]
    #  복사
    for i in range(A):
        for j in range(B):
            tmp[i][j] = paper[i][j]

    for i in range(B):
        for j in range(A):
            paper[i][j] = tmp[A-1-j][i]

    return B, A

# 붙일수있는지 체크, 붙일수있으면 붙이고 리턴


def possible(x, y):
    for i in range(A):
        for j in range(B):
            if board[x+i][y+j] == 1 and paper[i][j] == 1:
                return False

    for i in range(A):
        for j in range(B):
            if paper[i][j] == 1:
                board[x+i][y+j] = 1

    return True


N, M, K = map(int, input().split())
mn = float('inf')
board = [[0]*M for _ in range(N)]
for _ in range(K):
    A, B = map(int, input().split())

    # 회전위해 넉넉히
    paper = [[0]*12 for _ in range(12)]

    # 입력
    for i in range(A):
        li = list(map(int, input().split()))
        for j in range(B):
            paper[i][j] = li[j]

    for rot in range(4):
        is_possible = False
        for x in range(N-A+1):
            if is_possible:
                break
            for y in range(M-B+1):
                if possible(x, y):
                    is_possible = True
                    break
        if is_possible:
            break

        A, B = rotate(A, B)


print(int(sum(1 for i in range(N) for j in range(M) if board[i][j] == 1)))
