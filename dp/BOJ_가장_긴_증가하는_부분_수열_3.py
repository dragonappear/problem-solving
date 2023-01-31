# https://www.acmicpc.net/problem/12738
from sys import stdin,stdout
from bisect import bisect_left
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().strip().split()))
d=[A[0]] # d[i]=길이가 i인 LIS들의 마지막 원소 중 가장 작은 값

for i in range(1,N):
    if d[-1]<A[i]: # 길이가 k-1인 LIS의 마지막 수보다 더 크므로 길이가 k인 LIS를 만들수있다.
        d.append(A[i])
    else:
        idx=bisect_left(d,A[i])
        d[idx]=A[i]

print(len(d))