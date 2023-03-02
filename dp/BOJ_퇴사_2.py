# https://www.acmicpc.net/problem/15486
from sys import stdin
input = stdin.readline

N = int(input())
arr = [(0, 0)]

for _ in range(N):
    t, p = map(int, input().split())
    arr.append((t, p))

# 1. i번째 날부터 N번째 날까지 최대 수익
# 3. 초기값 0
d = [0]*(N+10)

for i in range(N, 0, -1):
    en = i+arr[i][0]-1
    if en > N:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], d[en+1]+arr[i][1])  # 2. 점화식

print(d[1])
