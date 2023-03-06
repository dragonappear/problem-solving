# https://www.acmicpc.net/problem/9663
from sys import stdin
input = stdin.readline


def dfs(row):
    global ans

    if row == N:
        ans += 1
        return

    for i in range(N):
        if col[i] or diag1[row+i] or diag2[row-i+N-1]:
            continue

        col[i] = diag1[row+i] = diag2[row-i+N-1] = True
        dfs(row+1)
        col[i] = diag1[row+i] = diag2[row-i+N-1] = False


N = int(input())

ans = 0
col = [False]*(N+1)
diag1 = [False]*(2*N)
diag2 = [False]*(2*N)

dfs(0)

print(ans)
