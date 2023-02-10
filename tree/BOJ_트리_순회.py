# https://www.acmicpc.net/problem/1991
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def levelorder(cur):
    q = deque([cur])
    while q:
        u = q.popleft()
        print(u, end='')
        for v in [lt[ord(u)-65], rt[ord(u)-65]]:
            if v == '.':
                continue
            q.append(v)


def preorder(cur):

    print(cur, end='')
    if lt[ord(cur)-65] != '.':
        preorder(lt[ord(cur)-65])
    if rt[ord(cur)-65] != '.':
        preorder(rt[ord(cur)-65])


def inorder(cur):

    if lt[ord(cur)-65] != '.':
        inorder(lt[ord(cur)-65])
    print(cur, end='')
    if rt[ord(cur)-65] != '.':
        inorder(rt[ord(cur)-65])


def postorder(cur):

    if lt[ord(cur)-65] != '.':
        postorder(lt[ord(cur)-65])
    if rt[ord(cur)-65] != '.':
        postorder(rt[ord(cur)-65])
    print(cur, end='')


N = int(input())
lt = [-1]*(N)
rt = [-1]*(N)
for _ in range(N):
    p, l, r = input().strip().split()
    lt[ord(p)-65] = l
    rt[ord(p)-65] = r

# levelorder('A')
# print()
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
