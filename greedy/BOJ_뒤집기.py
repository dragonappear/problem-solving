# https://www.acmicpc.net/problem/1439
from sys import stdin
input = stdin.readline

S = list(map(int, input().strip()))
N = len(S)
cnt = [0, 0]

cnt[S[0]] += 1

for i in range(1, N):
    if S[i] != S[i-1]:
        cnt[S[i]] += 1

print(min(cnt))
