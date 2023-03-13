# https://www.acmicpc.net/problem/1759
from sys import stdin
input = stdin.readline


def dfs(idx, word, mo, ja):
    if len(word) == L:
        if mo >= 1 and ja >= 2:
            print(word)
        return

    for i in range(idx, C):
        c = letters[i]

        if c in set:
            dfs(i+1, word+c, mo+1, ja)
        else:
            dfs(i+1, word+c, mo, ja+1)


L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
set = set(['a', 'e', 'i', 'o', 'u'])

dfs(0, "", 0, 0)
