# https://www.acmicpc.net/problem/2075
from sys import stdin,stdout
from heapq import heappush,heappop
input,write=stdin.readline,stdout.write


"""
풀이1: 힙

time:O(N^2*logN) n=[1,1500]
space: O(N) n=[1,1500]
"""
N=int(input())
heap = []
for _ in range(N): # O(N^2)
    for n in list(map(int,input().strip().split())):
        if len(heap)<N:
            heappush(heap,n)
        else:
            if heap[0]<n: # O(logN)
                heappop(heap)
                heappush(heap,n)
print(heap[0])
        

"""
풀이2: 정렬

time:O(N^2*logN) n=[1,1500]
space: O(N) n=[1,1500]
"""
N=int(input())
arr = []
for _ in range(N):
    for a in list(map(int,input().strip().split())):
        arr.append(a)
    arr = sorted(arr,reverse=True)[:N]
print(arr[N-1])