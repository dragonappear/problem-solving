# https://www.acmicpc.net/problem/2250
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def visit(p, r):
    def set_pos():
        global col
        level[r].append(col)
        col += 1

    if left[p] == -1 and right[p] == -1:  # 리프 노드
        set_pos()
        return

    if left[p] != -1:  # 왼쪽 자식
        visit(left[p], r+1)

    set_pos()

    if right[p] != -1:  # 오른쪽 자식
        visit(right[p], r+1)


N = int(input())
left, right, parent = [-1]*(N+1), [-1]*(N+1), [-1]*(N+1)
level = [[] for _ in range(N+1)]
col = 0

# 입력
for i in range(N):
    c, l, r = map(int, input().split())
    left[c] = l
    right[c] = r
    if l != -1:
        parent[l] = c
    if r != -1:
        parent[r] = c

# 부모 노드
for i in range(1, N+1):
    if parent[i] == -1:
        root = i
        break

visit(root, 0)

mx, idx = float('-inf'), 0
for i, v in enumerate(level):
    if not v:
        continue
    w = v[-1]-v[0]+1
    if w > mx:
        idx = i
        mx = w

print(idx+1, mx)
