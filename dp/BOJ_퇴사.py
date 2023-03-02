# https://www.acmicpc.net/problem/14501
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def dfs(idx, sm):
    global mx

    if mx < sm:
        mx = sm

    for i in range(idx+1, N+1):
        if i+arr[i][0]-1 <= N:
            dfs(i+arr[i][0]-1, sm+arr[i][1])


N = int(input())
arr = [(0, 0)]

for _ in range(N):
    t, p = map(int, input().split())
    arr.append((t, p))

mx = 0

for i in range(1, N+1):
    if i+arr[i][0]-1 <= N:
        dfs(i+arr[i][0]-1, arr[i][1])

print(mx)
