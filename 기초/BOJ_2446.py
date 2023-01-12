import sys
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    filled = " " * (i-1)
    stars = "*"* (N-i+1)
    plus = "*"* (N-i)
    print( filled + stars+plus)

for i in range(1,N):
    filled = " " * (N-i-1)
    stars = "*"* (i+1)
    plus = "*"* (i)
    print( filled  + stars + plus)