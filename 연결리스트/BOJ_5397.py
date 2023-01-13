from sys import stdin,stdout
from collections import deque
input = stdin.readline
write = stdout.write

answer = []
for _ in range(int(input())):
    commands = list(input().strip())
    deque1,deque2 = deque(),deque()
    
    for command in commands:
        if command=="<":
            if deque1:
                deque2.appendleft(deque1.pop())
        elif command==">":
            if deque2:
                deque1.append(deque2.popleft())
        elif command.isalnum():
                deque1.append(command)
        elif command=="-":
            if deque1:
                deque1.pop()
    answer.append(''.join(deque1+ deque2))

for a in answer:
    write(a+"\n")