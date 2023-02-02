# https://www.acmicpc.net/problem/2003
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=list(map(int,input().strip().split()))
lt=rt=cnt=sum=0

while True:
    if sum>=M: 
        sum-=A[lt]
        lt+=1
    elif rt==N: 
        break
    else: 
        sum+=A[rt]
        rt+=1
        
    if sum==M:
        cnt+=1
    
print(cnt)