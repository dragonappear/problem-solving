# https://www.acmicpc.net/problem/1655
from heapq import heappush,heappop
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

max_heap,min_heap=[],[]
answer=[]
for _ in range(int(input())):
    n=int(input())
    if not max_heap and not min_heap:
        max_heap.append(-n)
    elif len(max_heap)>len(min_heap):
        if -max_heap[0]<n:
            heappush(min_heap,n)
        else:
            heappush(max_heap,-n)
            heappush(min_heap,-heappop(max_heap))
    elif len(max_heap)==len(min_heap):
        if -max_heap[0]<n:
            heappush(min_heap,n)
            heappush(max_heap,-heappop(min_heap))
        else:
            heappush(max_heap,-n)
            
    write(str(-max_heap[0])+"\n")