from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write
deq = deque()

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == "push_front": deq.appendleft(int(cmd[1]))        
    elif cmd[0] == "push_back": deq.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if not deq: write('-1\n')
        else: write(str(deq.popleft())+"\n")
    elif cmd[0] == "pop_back":
        if not deq: write('-1\n')
        else: write(str(deq.pop())+"\n")
    elif cmd[0] == "size": write(str(len(deq))+"\n")
    elif cmd[0] == "empty":
        if not deq: write("1\n")
        else: write("0\n")
    elif cmd[0] == "front":
        if not deq: write("-1\n")
        else: write(str(deq[0])+"\n")
    elif cmd[0] == "back":
        if not deq: write("-1\n")
        else: write(str(deq[-1])+"\n")