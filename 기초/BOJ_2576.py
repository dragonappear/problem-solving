import sys
input = sys.stdin.readline

odds = [n for n in [int(input()) for _ in range(7) ] if n%2!=0]
if not odds:
    print(-1)
else:
    print(sum(odds),min(odds),sep='\n')