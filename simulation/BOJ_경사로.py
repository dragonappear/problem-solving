# https://www.acmicpc.net/problem/14890
from sys import stdin
input = stdin.readline


def calc(arr):

    p = 0
    cnt = 1   # 현재보고 있는 수와 높이가 같은 구간의 길이
    while p < N-1:
        if abs(arr[p+1]-arr[p]) > 1:
            return 0

        if arr[p+1] == arr[p]:
            cnt += 1
            p += 1
        elif arr[p+1] > arr[p]:
            if cnt < L:
                return 0
            p += 1
            cnt = 1
        elif arr[p+1] < arr[p]:
            if p+L >= N:
                return 0
            for i in range(p+2, p+L+1):
                if arr[p+1] != arr[i]:
                    return 0
            p += L
            cnt = 0

    return 1


N, L = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
ans = 0

for i in range(N):
    ans += calc(board[i])
    ans += calc([board[j][i] for j in range(N)])

print(ans)
