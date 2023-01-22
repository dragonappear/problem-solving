# https://www.acmicpc.net/problem/19583
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

memberset=set()
S,E,Q=input().split()
count=0
while True:
    s=input().strip()
    if s=='': break
    
    time,nickname = s.split()
    if time<=S:
        memberset.add(nickname)
    elif E<=time<=Q:
        if nickname in memberset:
            count+=1
            memberset.remove(nickname)
            
write(str(count)+"\n")
    