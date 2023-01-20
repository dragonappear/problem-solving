# https://www.acmicpc.net/problem/2800
from itertools import combinations
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
1.조합

괄호쌍 정보를 저장한 후, 조합으로 생성하여 결과추출
time:O(n!) n=[1,10] n is the number of pairs
space:O(n) n=[1,10] n is the number of pairs
"""
expression=input().strip()
result=set()

pair,stack=[],[]
for i,c in enumerate(expression): # 괄호쌍 저장 O(n)
    if c=="(":
        stack.append(i)
    elif c==")":
        start = stack.pop()
        pair.append((start,i))

for i in range(1,len(pair)+1): # O(n)
    comb =  combinations(pair,i) #O(n!)
    for c in comb:
        tmp=list(expression)
        for start,end in c:
            tmp[start]=tmp[end]=''
        result.add(''.join(tmp))

for i in sorted(list(result)):
    write(i+"\n")