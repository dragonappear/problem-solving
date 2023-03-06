# https://www.acmicpc.net/problem/1212
from sys import stdin
input = stdin.readline

N = int(input(), 8)
print(bin(N)[2:])
