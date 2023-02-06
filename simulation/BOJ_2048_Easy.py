# https://www.acmicpc.net/problem/12100
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


N = int(input())
board1 = [list(map(int, input().split())) for _ in range(N)]
board2 = [element[:] for element in board1]

mx = 0
