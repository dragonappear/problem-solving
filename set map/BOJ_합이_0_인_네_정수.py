# https://www.acmicpc.net/problem/7453
from sys import stdin
input = stdin.readline

N = int(input())
A, B, C, D = [0]*N, [0]*N, [0]*N, [0]*N
cnt = 0
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

AB = []
for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])

CD = dict()
for i in range(N):
    for j in range(N):
        s = C[i]+D[j]
        if s in CD:
            CD[s] += 1
        else:
            CD[s] = 1


for x in AB:
    if -x in CD:
        cnt += CD[-x]

print(cnt)
