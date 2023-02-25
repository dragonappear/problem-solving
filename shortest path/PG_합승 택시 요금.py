# https://school.programmers.co.kr/learn/courses/30/lessons/72413
INF = float('inf')


def solution(n, s, a, b, fares):

    dist = [[INF] * n for _ in range(n)]
    nxt = [[-1] * n for _ in range(n)]

    for u, v, w in fares:
        dist[u-1][v-1] = w
        dist[v-1][u-1] = w

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]

    mn = INF
    for i in range(n):
        t = dist[s-1][i] + dist[i][a-1] + dist[i][b-1]
        mn = min(mn, t)

    return mn
