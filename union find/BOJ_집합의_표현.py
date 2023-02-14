# https://www.acmicpc.net/problem/1717
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        if a != b:
            union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
