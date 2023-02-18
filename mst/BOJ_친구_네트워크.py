# https://www.acmicpc.net/problem/4195
from sys import stdin
from collections import defaultdict
input = stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        parent[y] = x
        nums[x] += nums[y]
        return nums[x]
    else:
        parent[x] = y
        nums[y] += nums[x]
        return nums[y]


for _ in range(int(input())):

    F = int(input())
    parent = defaultdict(str)
    nums = defaultdict(int)
    for _ in range(F):
        a, b = input().split()
        if parent[a] == "":
            parent[a] = a
            nums[a] = 1
        if parent[b] == "":
            parent[b] = b
            nums[b] = 1

        if find(a) == find(b):
            print(nums[parent[a]])
            continue

        print(union(a, b))
