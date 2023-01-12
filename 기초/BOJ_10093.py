import sys
input = sys.stdin.readline

a,b=map(int,input().split())

if a==b:
    print(0)
    print()
else:
    a,b=min(a,b),max(a,b)
    print(b-a-1)
    print(*[n for n in range(a+1,b)])