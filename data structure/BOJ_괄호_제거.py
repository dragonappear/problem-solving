# https://www.acmicpc.net/problem/2800
from sys import stdin,stdout
from itertools import combinations
input,write=stdin.readline,stdout.write

"""
DFS

time: O(2^10)
space: O(N) n=[1,200]
"""

def dfs(rst:str,idx:int):
    
    if idx==len(s):
        if rst!=s:
            result.add(rst)
        return
    
    if s[idx]== '(':
        visit[idx]=True
        dfs(rst+'(', idx+1)
        visit[idx]=False
        dfs(rst, idx+1)
    elif s[idx]== ')':
        if visit[pair_map[idx]]:
            dfs(rst + ')',idx+1)
        else:
            dfs(rst,idx+1)
    else:
        dfs(rst+s[idx],idx+1)


s=input().strip()
pair_map = dict()
visit=[False]*len(s)

stack=[]
for i, v in enumerate(s):
    if v == '(': stack.append(i)
    elif v == ')': pair_map[i]= stack.pop()

result=set()             
dfs("",0)
for r in sorted(list(result)):
    write(r+"\n")
    
    
"""
조합

괄호쌍 정보를 저장한 후, 조합으로 생성하여 결과추출
time:O(n!)
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