import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    filled = " " * i
    print( filled  + "*"* (N-i) + "*"*(N-i-1))