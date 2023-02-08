# https://www.acmicpc.net/problem/14888
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def dfs(idx, tot):
    global mx, mn

    if idx == N:
        mx, mn = max(mx, tot), min(mn, tot)
        return

    for op, v in enumerate(operators):
        if v == 0:
            continue
        operators[op] -= 1
        if op == 0:
            dfs(idx+1, tot+A[idx])
        elif op == 1:
            dfs(idx+1, tot-A[idx])
        elif op == 2:
            dfs(idx+1, tot*A[idx])
        else:
            dfs(idx+1, int(tot/A[idx]))
        operators[op] += 1


N = int(input())
A = list(map(int, input().strip().split()))
operators = list(map(int, input().split()))
mx, mn = float('-inf'), float('inf')

dfs(1, A[0])
print(mx)
print(mn)
