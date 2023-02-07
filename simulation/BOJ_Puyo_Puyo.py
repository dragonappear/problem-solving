# https://www.acmicpc.net/problem/11559
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write

board = [list(input().strip()) for _ in range(12)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
tot = int(sum(1 for i in range(12)
              for j in range(6) if board[i][j] != '.'))
ans = 0
while True:

    visit = [[False]*6 for _ in range(12)]
    pop = False
    # 1. 마크
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] == '.' or visit[i][j]:
                continue
            q = deque([(i, j)])
            visit[i][j] = True
            trace = set()
            trace.add((i, j))
            while q:
                r, c = q.popleft()
                for dr, dc in dr_dc:
                    nr, nc = r+dr, c+dc
                    if not(0 <= nr < 12) or not(0 <= nc < 6) or visit[nr][nc] or board[nr][nc] != board[i][j]:
                        continue
                    visit[nr][nc] = True
                    trace.add((nr, nc))
                    q.append((nr, nc))
            # 2. 제거
            if len(trace) >= 4:
                for a, b in trace:
                    board[a][b] = '.'
                pop = True
    # 아래로
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] == '.':
                continue
            if i+1 <= 11 and board[i+1][j] == '.':
                x = i
                while x <= 10 and board[x+1][j] == '.':
                    x += 1
                board[x][j], board[i][j] = board[i][j], '.'

    if pop:
        ans += 1
    else:
        break

rst = int(sum(1 for i in range(12)
              for j in range(6) if board[i][j] != '.'))

print(ans if tot != rst else 0)
