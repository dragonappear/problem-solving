# https://www.acmicpc.net/problem/2887
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
parent = [i for i in range(N)]
x, y, z = [], [], []
nodes = [list(map(int, input().split())) for _ in range(N)]
for i, node in enumerate(nodes):
    x.append((node[0], i))
    y.append((node[1], i))
    z.append((node[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(0, N-1):
    edges.append((x[i+1][0]-x[i][0], x[i+1][1], x[i][1]))
    edges.append((y[i+1][0]-y[i][0], y[i+1][1], y[i][1]))
    edges.append((z[i+1][0]-z[i][0], z[i+1][1], z[i][1]))


edges.sort()

rst = cnt = 0

for i in range(len(edges)):
    dist, a, b = edges[i]
    if find(a) == find(b):
        continue
    union(a, b)
    rst += dist

print(rst)


"""
간선의 가중치가 될 수 있는 값을 찾아놓는 것이 핵심
"""
