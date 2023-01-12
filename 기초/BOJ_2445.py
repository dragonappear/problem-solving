import sys
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    stars = '*' * i
    filled = " " * 2*(N-i)
    print(stars + filled + stars)

for i in range(1,N):
    stars = '*' * (N-i)
    filled = " " * 2*(i)
    print(stars + filled + stars)

