from sys import stdin,stdout
from collections import deque
input = stdin.readline
write = stdout.write

queue = deque([i for i in range(1,int(input())+1)])

if len(queue)<=2:
    write(str(len(queue)))
    exit()    

while queue:  
    queue.popleft() 
    if len(queue)==1:
        write(str(queue[0]))
        exit()
    if queue: 
        x = queue.popleft()
        queue.append(x)