import sys
input = sys.stdin.readline

mx = float('-inf')
index = 0
for i in range(9):
    n = int(input())
    if mx < n:
        mx = n
        index = i

print(mx,index+1,sep='\n')
