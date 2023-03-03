# https://www.acmicpc.net/problem/2217
from sys import stdin
input = stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()
mx = -1
for i in range(N):
    mx = max(mx, rope[i]*(N-i))

print(mx)
