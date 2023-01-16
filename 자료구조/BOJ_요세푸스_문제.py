from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

"""
n명의 사람이 있고, k를 주기로 사람을 제거하면 된다
주기가 사람의 인원수를 초과하면 사람의 인원수로 나눈 나머지로 값을 초기화한다

time: O(n^2) n=[1,5_000]
space: O(n) n=[1,5_000]
"""

n,k=map(int,input().split())
arr = [i for i in range(1,n+1)]

answer = [] # 제거된 사람들을 저장하는 배열
index = 0 # 제거될 사람의 인덱스 번호

for _ in range(n):
    index += k-1
    if index >= len(arr):
        index = index%len(arr)
    
    answer.append(str(arr.pop(index)))

print("<",", ".join(answer),">",sep='')