import sys
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    filled = " "* (N-i)
    stars="*"*i
    print(filled+stars)
    
