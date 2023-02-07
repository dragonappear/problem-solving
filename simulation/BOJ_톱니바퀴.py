# https://www.acmicpc.net/problem/14891
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def solve(n, d):
    # 회전 변수
    dirs = [0]*4
    dirs[n] = d

    # 왼쪽으로 회전을 전파
    idx = n
    while idx > 0 and wheel[idx][6] != wheel[idx-1][2]:
        dirs[idx-1] = -dirs[idx]
        idx -= 1

    # 오른쪽으로 회전 전파
    idx = n
    while idx < 3 and wheel[idx][2] != wheel[idx+1][6]:
        dirs[idx+1] = -dirs[idx]
        idx += 1

    for i in range(4):
        if dirs[i] == -1:
            x = wheel[i].pop(0)
            wheel[i].append(x)

        elif dirs[i] == 1:
            x = wheel[i].pop()
            wheel[i].insert(0, x)


wheel = [list(map(int, input().strip())) for _ in range(4)]

for _ in range(int(input())):
    n, d = map(int, input().split())
    solve(n-1, d)

score = 0
for i in range(4):
    if wheel[i][0] == 1:
        score += (1 << i)

print(score)
