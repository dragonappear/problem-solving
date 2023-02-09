# https://www.acmicpc.net/problem/14890
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def check(line):
    idx = 0
    cnt = 1  # 현재보고 잇는, 높이가 같은 구간의 길이

    while idx < (N-1):
        if abs(line[idx+1]-line[idx]) > 1:  # 높이 차이가 1 이상이면 불가능
            return 0

        if line[idx] == line[idx+1]:
            cnt += 1
            idx += 1

        elif line[idx] < line[idx+1]:
            if cnt < L:  # L보다 작아서 경사로를 놓을 수 없음
                return 0
            cnt = 1
            idx += 1

        else:
            if idx+L >= N:
                return 0
            for i in range(idx+1, idx+L):
                if line[i] != line[i+1]:
                    return 0
            idx = idx+L
            cnt = 0
    return 1


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 가로
for i in range(N):
    line = []
    for j in range(N):
        line.append(board[i][j])
    ans += check(line)
# 세로
for i in range(N):
    line = []
    for j in range(N):
        line.append(board[j][i])
    ans += check(line)

print(ans)
