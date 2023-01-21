# https://www.acmicpc.net/problem/1406
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

s=input().strip()
left,right=deque(s),deque()

for _ in range(int(input())):
    cmd = input().split()
    c = cmd[0]
    
    if c=="P":
        left.append(cmd[1])
    elif c=="B":
        if left: left.pop()
    elif c=="D":
        if right: left.append(right.popleft())
    elif c=="L":
        if left: right.appendleft(left.pop())

write(''.join(list(left+right)))