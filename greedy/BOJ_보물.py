# https://www.acmicpc.net/problem/1026
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split())) # B 재배열 X
A.sort()
B.sort(reverse=True)
cnt=0
for i in range(N):
    cnt+= (A[i]*B[i])
print(cnt)