# https://www.acmicpc.net/problem/1700
from sys import stdin,stdout
from collections import Counter
input,write=stdin.readline,stdout.write

N,K=map(int,input().split())
A=list(map(int,input().split()))
counter=Counter(A)
plug=set()
cnt=0
for i,n in enumerate(A):
    if n in plug: 
        counter[n]-=1
        continue
    
    if len(plug)<=N-1: # 공간이 있으면 그냥 꽂기
        plug.add(n)
        counter[n]-=1
        
    elif len(plug)==N: # 교체해야 하는 경우
        cnt+=1 
        
        # 1. 꽂은것중 나중에 가장 안쓰이는 것 교체
        escape=False
        counter[n]-=1
        for m in plug:
            if counter[m]==0:
                plug.remove(m)
                plug.add(n)
                escape=True
                break
        if escape: continue
        
        # 2. 안쓰이는 것이 없으면 나중에 가장 늦게 꽂는 것 교체
        last=set()
        val=-1
        for j in range(i+1,len(A)):
            if A[j] in plug and A[j] not in last:
                last.add(A[j])
                val=A[j]
        if val==-1: 
            plug.pop()
        else: 
            plug.remove(val)
        plug.add(n)
        
print(cnt)

"""
풀이
1.멀티탭에 꽂혀있는 물건 중 이후에 꽂지 않는 제품과 교체
2.멀티탭에 꽂혀있는 물건 중 가장 나중에 꽂는 제품과 교체
"""