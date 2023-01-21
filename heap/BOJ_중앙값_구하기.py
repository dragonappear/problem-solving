# https://www.acmicpc.net/problem/2696
from sys import stdin,stdout
from heapq import heappop,heappush
input,write=stdin.readline,stdout.write


"""
힙
"""
for T in range(int(input())):
    M=int(input())
    arr=[]
    for _ in range((M//10)+1):
        arr.extend(list(map(int,input().strip().split())))
    max_q=[] # max_q=중앙값 + 중앙값 미만의 값
    min_q=[] # min_q= 중앙값 초과 값
    answer=[]
    for i in range(1,len(arr)+1):
        number=arr[i-1]
        if not max_q and not min_q: 
            max_q.append(-number) # 초기 상태
            
        elif len(max_q)>len(min_q):
            # 들어온 수가 현재 중앙값보다 작다면 중앙값 교체    
            # max_q top을 min_q로 이동
            if -max_q[0]>arr[i-1]: 
                heappush(max_q,-number)
                heappush(min_q,-heappop(max_q))
            # 아니면 min_q로 이동
            else:  
                heappush(min_q,number)
            
        elif len(max_q)==len(min_q):
            # 들어온 수가 현재 중앙값 크면
            if -max_q[0] < number:
                heappush(min_q,number)
                heappush(max_q,-heappop(min_q))
            else:
                heappush(max_q,-number)
        
        if i%2:
            answer.append(-max_q[0])
    
    print(len(arr)//2 + 1)
    for i,v in enumerate(answer):
        print(v,end=' ')
        if (i+1)%10==0:
            print()
    print()