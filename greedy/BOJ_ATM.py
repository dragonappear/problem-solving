# https://www.acmicpc.net/problem/11399
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().strip().split()))

A.sort()

total=0
prev=0
for i in range(N):
    prev+=A[i]
    total+=prev

print(total)