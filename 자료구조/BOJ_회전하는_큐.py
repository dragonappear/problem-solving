from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

for _ in range(int(input())):
    cmds = input().strip() # [1,10^5]
    n = int(input()) # [1,10^5]
    temp = input().strip()
    arr = deque([int(c) for c in temp[1:len(temp)-1].split(',') if c.isdigit()])
    flag = True
    direciton = 0

    for cmd in cmds: # [1,10^5]
        if cmd=="R":
            if direciton==0: direciton=1
            else: direciton=0
        elif cmd=="D":
            if not arr:
                flag = False
                break
            else:
                if direciton==0: arr.popleft()
                else: arr.pop()
    
    if flag:
        write("[")
        if direciton==1:
            for i in range(len(arr)-1,-1,-1):
                if i == 0:
                    write(str(arr[i]))
                    break
                write(str(arr[i])+",")
        else:
            for i in range(len(arr)):
                if i == len(arr)-1:
                    write(str(arr[i]))
                    break
                write(str(arr[i])+",")
        write("]\n")
    else:
        write("error\n")
