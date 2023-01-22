# https://www.acmicpc.net/problem/4358
from sys import stdin,stdout
from collections import Counter
input,write=stdin.readline,stdout.write

tset=set()
tlist=[]
total=0
while True:
    name = input().strip()
    if name=='': break
    tset.add(name)
    tlist.append(name)
    total+=1
    
counter=Counter(tlist)

for tree in sorted(list(tset)):
    ratio = (counter[tree]/total)*100
    print(f'{tree} {ratio:.4f}')