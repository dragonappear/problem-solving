# https://www.acmicpc.net/problem/7662
from heapq import heappush,heappop
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

result=[]
for T in range(int(input())):
    visited=[False]*1_000_001
    min_heap,max_heap=[],[]
    for i in range(int(input())):
        s=input().split()
        cmd,value=s[0],int(s[1])
        
        if cmd=='I':
            heappush(min_heap,(value,i))
            heappush(max_heap,(-value,i))
            visited[i]=True
            
        elif value==1:
            while max_heap and not visited[max_heap[0][1]]: # 동기화 부분
                heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]]=False
                heappop(max_heap)
        else:
            while min_heap and not visited[min_heap[0][1]]: # 동기화 부분
                heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]]=False
                heappop(min_heap)
    
    while min_heap and not visited[min_heap[0][1]]: # 동기화 부분
        heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]: # 동기화 부분
        heappop(max_heap)
        
    if max_heap and min_heap:
        write(str(-max_heap[0][0]) + " " + str(min_heap[0][0])+"\n")
    else:
        write("EMPTY\n")
