from sys import stdin,stdout
from collections import deque
input = stdin.readline
write = stdout.write

queue1,queue2 = deque(list(input().strip())),deque()
cmds = [ input().strip() for _ in range(int(input()))]

for cmd in cmds:
    if cmd[0]=="P":
        queue1.append(cmd[2])
    elif cmd[0]=="L":
        if queue1:
            queue2.appendleft(queue1.pop())
    elif cmd[0]=="D":
        if queue2:
            queue1.append(queue2.popleft())
    elif cmd[0]=="B":
        if queue1:
            queue1.pop()

write(''.join(queue1)+''.join(queue2))