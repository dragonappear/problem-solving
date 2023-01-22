# https://www.acmicpc.net/problem/17255
from sys import stdin,stdout
from typing import List
input,write=stdin.readline,stdout.write


def dfs(ret:List,depth:int,history:str):
    global count
    
    if depth==len(N):
        if ret==N and history not in historyset: 
            count+=1
            historyset.add(history)
        return
    
    for i in range(len(N)):
        if ret[i]!=-1 : continue
        if depth != 0 and (( 0<i<len(N)-1 and ret[i-1]==-1 and ret[i+1]==-1) or (i==0 and ret[i+1]==-1) or (i==len(N)-1 and ret[i-1]==-1)): continue
        ret[i]=N[i]
        s = ''.join([str(c) for c in ret if c!=-1])
        dfs(ret,depth+1,history+s)
        ret[i]=-1

N=list(map(int,input().strip()))
count = 0
rst=[-1]*len(N)
historyset=set()
dfs(rst,0,"")
write(str(count))