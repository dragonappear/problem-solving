# https://www.acmicpc.net/problem/9934
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def visit(arr, depth):
    if depth == K-1:
        level[depth].append(arr[0])
        return

    mid = len(arr)//2
    visit(arr[:mid], depth+1)
    visit(arr[mid+1:], depth+1)
    level[depth].append(arr[mid])


K = int(input())
arr = list(map(int, input().split()))
level = [[] for _ in range(K)]
visit(arr, 0)
for lev in level:
    print(*lev)

"""
중위순회
"""
