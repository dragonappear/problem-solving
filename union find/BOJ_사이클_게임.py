# https://www.acmicpc.net/problem/20040
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().strip().split())
parent = [i for i in range(0, N)]


idx = 0
for i in range(1, M+1):
    x, y = map(int, input().strip().split())
    if find(x) == find(y):
        idx = i
        break
    union(x, y)

print(idx)
