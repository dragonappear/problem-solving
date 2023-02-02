# https://www.acmicpc.net/problem/2230
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=[int(input()) for _ in range(N)]
A.sort()
lt,rt=0,0

mn=float('inf')
while lt<N and rt<N and lt<=rt:
    diff=A[rt]-A[lt]
    
    if diff==M:
        print(M)
        exit()
    elif diff>M:
        mn=min(mn,diff)
        lt+=1
    elif diff<M:
        rt+=1
        
print(mn)