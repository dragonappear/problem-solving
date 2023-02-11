# https://www.acmicpc.net/problem/14891
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def get_scrore():
    ans = 0
    for i in range(4):
        if wheels[i][0]:
            ans += (1 << i)
    return ans


def rotate(n, d):
    wheel = wheels[n]
    if d == 1:
        x = wheel.pop()
        wheel.insert(0, x)
    else:
        x = wheel.pop(0)
        wheel.append(x)


def solve(n, d):
    rot = [(n, d)]

    dd = d
    for i in range(n, 0, -1):
        if wheels[i][6] == wheels[i-1][2]:
            break
        rot.append((i-1, -dd))
        dd *= -1

    dd = d
    for i in range(n, 3):
        if wheels[i][2] == wheels[i+1][6]:
            break
        rot.append((i+1, -dd))
        dd *= -1

    for nn, dd in rot:
        rotate(nn, dd)


wheels = [list(map(int, input().strip())) for _ in range(4)]
for _ in range(int(input())):
    N, D = map(int, input().strip().split())
    solve(N-1, D)

print(get_scrore())
