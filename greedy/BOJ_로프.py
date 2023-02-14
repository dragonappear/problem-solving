# https://www.acmicpc.net/problem/2217
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


N = int(input())
ROPE = sorted([int(input()) for _ in range(N)])
ans = 0
for i in range(1, N+1):
    ans = max(ans, ROPE[N-i]*i)
print(ans)
