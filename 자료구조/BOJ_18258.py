from sys import stdin,stdout
from collections import deque
input = stdin.readline
write = stdout.write

queue,size = deque(),0
for _ in range(int(input())):
    command = input().split()

    if command[0] == "push":
        queue.append(int(command[1]))
        size+=1
    elif command[0] == "pop":
        if size==0:
            write(str(-1)+"\n")
            continue
        size-=1
        write(str(queue.popleft())+"\n")
    elif command[0] == "size":
        write(str(size)+"\n")
    elif command[0] == "empty":
        if size==0:
            write(str(1)+"\n")
            continue
        write(str(0)+"\n")
    elif command[0] == "front":
        if size==0:
            write(str(-1)+"\n")
            continue
        write(str(queue[0])+"\n")
    elif command[0] == "back":
        if size==0:
            write(str(-1)+"\n")
            continue
        write(str(queue[-1])+"\n")
