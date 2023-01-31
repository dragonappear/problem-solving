# https://www.acmicpc.net/problem/12015
from sys import stdin,stdout
from bisect import bisect_left
input,write=stdin.readline,stdout.write

def binary_search(val):
    ret=float('inf')
    left,right=0,len(d)-1
    while left<=right:
        mid=(left+right)//2
        if d[mid]>=val:
            if ret>mid: ret=mid
            right=mid-1
        else:
            left=mid+1
    return ret

N=int(input())
A=list(map(int,input().strip().split()))
d=[A[0]] # d[i]=길이가 i인 LIS들의 마지막 원소 중 가장 작은 값

for i in range(1,N):
    if d[-1]<A[i]: # 길이가 k-1인 LIS의 마지막 수보다 더 크므로 길이가 k인 LIS를 만들수있다.
        d.append(A[i])
    else:
        # 풀이1
        idx=bisect_left(d,A[i])
        
        # 풀이2
        idx=binary_search(A[i])
        d[idx]=A[i]

print(len(d))