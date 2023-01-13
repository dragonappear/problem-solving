from sys import stdin,stdout
input = stdin.readline
write = stdout.write

stack,size = [],0
for _ in range(int(input())):
    command = input().split()

    if command[0] == "push":
        stack.append(int(command[1]))
        size+=1
    elif command[0] == "pop":
        if not stack:
            write(str(-1)+"\n")
            continue
        size-=1
        write(str(stack.pop())+"\n")
    elif command[0] == "size":
        write(str(size)+"\n")
    elif command[0] == "empty":
        if not stack:
            write(str(1)+"\n")
            continue
        write(str(0)+"\n")
    elif command[0] == "top":
        if not stack:
            write(str(-1)+"\n")
            continue
        write(str(stack[-1])+"\n")
