# https://www.acmicpc.net/problem/11728
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
result=[]
ap=bp=0

while ap<N and bp<M:
    if A[ap]>B[bp]:
        result.append(B[bp])
        bp+=1
    else:
        result.append(A[ap])
        ap+=1
    
if ap==N:
    while bp<M:
        result.append(B[bp])
        bp+=1
elif bp==M:
    while ap<N:
        result.append(A[ap])
        ap+=1

print(*result)