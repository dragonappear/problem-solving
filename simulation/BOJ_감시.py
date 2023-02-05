# https://www.acmicpc.net/problem/15683
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def dfs(num, cp):
    global mn

    def fill():
        graph = [element[::] for element in cp]
        r, c = cctvs[num]
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            while (0 <= nr < N) and (0 <= nc < M) and graph[nr][nc] != 6:
                if graph[nr][nc] == 0:
                    graph[nr][nc] = -1
                nr, nc = nr+dr, nc+dc
        return graph

    if num == len(cctvs):
        blind = int(sum(1 for i in range(N)
                    for j in range(M) if cp[i][j] == 0))
        mn = min(mn, blind)
        return

    for dirs in actions[cp[cctvs[num][0]][cctvs[num][1]]]:
        dfs(num+1, fill())


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctvs = [(i, j) for i in range(N)
         for j in range(M) if board[i][j] >= 1 and board[i][j] != 6]
mn = int(sum(1 for i in range(N)
             for j in range(M) if board[i][j] == 0))
dr_dc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
actions = {
    1: [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
    2: [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(-1, 0), (0, -1), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(0, -1), (-1, 0), (1, 0)]],
    5: [[(-1, 0), (0, -1), (1, 0), (0, 1)]]
}
dfs(0, board)
print(mn)
