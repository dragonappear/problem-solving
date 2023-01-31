# https://www.acmicpc.net/problem/14003
from sys import stdin,stdout
from bisect import bisect_left
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().split()))
d=[A[0]] # d[i]=길이가i인 LIS들의 마지막원소의 최솟값
p=[0]*N # i번째 원소가 L내에서 위치하는 인덱스 저장
for i in range(1,N):
    if d[-1]<A[i]:
        d.append(A[i])
        p[i]=len(d)-1
    else:
        idx=bisect_left(d,A[i])
        d[idx]=A[i]
        p[i]=idx

print(len(d))
max_length=len(d)-1
answer=[]
for i in range(N-1,-1,-1):
    if p[i]==max_length:
        answer.append(A[i])
        max_length-=1
print(*reversed(answer))