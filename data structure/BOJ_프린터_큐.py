# https://www.acmicpc.net/problem/1966
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

# 중요도는 높은순서대로 출력
for _ in range(int(input())):
    N,M=map(int,input().split())
    rank=list(map(int,input().split()))
    arr=list(zip(rank,[i for i in range(0,N)]))
    rank.sort() 
    
    q = deque(arr)
    count=0
    while q:
        priority,index=q.popleft()
        if priority<rank[-1]:
            q.append((priority,index))
        elif priority==rank[-1]:
            rank.pop()
            count+=1
            if index==M: 
                break
    write(str(count)+"\n")