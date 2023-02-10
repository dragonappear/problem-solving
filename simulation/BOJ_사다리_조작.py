# https://www.acmicpc.net/problem/15684
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


# 사타리 타기
def check():
    for j in range(1, N+1):
        cur = j
        for i in range(1, H+1):
            if ladder[i][cur-1]:
                cur -= 1
            elif ladder[i][cur]:
                cur += 1
        if cur != j:
            return False
    return True


N, M, H = map(int, input().strip().split())
ladder = [[False]*12 for _ in range(32)]
coords = []  # 고를 수 있는 가로선만을 저장할 리스트

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = True

for i in range(1, H+1):
    for j in range(1, N):
        if ladder[i][j-1] or ladder[i][j] or ladder[i][j+1]:
            continue
        coords.append((i, j))

if check():
    print(0)
    exit()

ans = float('inf')
sz = len(coords)

for i in range(sz):
    ladder[coords[i][0]][coords[i][1]] = True
    if check():
        ans = min(ans, 1)
        if ans == 1:
            print(1)
            exit()

    for j in range(i+1, sz):
        ladder[coords[j][0]][coords[j][1]] = True
        if check():
            ans = min(ans, 2)

        for k in range(j+1, sz):
            ladder[coords[k][0]][coords[k][1]] = True
            if check():
                ans = min(ans, 3)

            ladder[coords[k][0]][coords[k][1]] = False

        ladder[coords[j][0]][coords[j][1]] = False

    ladder[coords[i][0]][coords[i][1]] = False

print(ans if ans != float('inf') else -1)
