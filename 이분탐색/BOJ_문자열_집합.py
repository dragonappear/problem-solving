from sys import stdin,stdout
from bisect import bisect_left
input,write=stdin.readline,stdout.write

"""

solution 1: 이분탐색
time: O(MNlogN) M=[1,10_000] N=[1,10_000]
space: O(N) N=[1,10_000]

solution 2: 트라이
"""
N,M=map(int,input().split())
arr,count = [],0

for _ in range(N):
    arr.append(input().strip())

arr.sort() #O(NlogN)

for _ in range(M): # O(M)
    input_str = input().strip()
    result = bisect_left(arr,input_str) # O(NlogN)
    if 0<=result<len(arr) and arr[result]==input_str:
        count+=1
    
write(str(count))