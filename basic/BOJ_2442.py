import sys
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    filled = " " * (N-i)
    print( filled  + "*"*i + "*"*(i-1))
    
