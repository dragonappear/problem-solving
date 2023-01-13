from sys import stdin,stdout
input = stdin.readline
write = stdout.write

stack = []

for _ in range(int(input())):
    x = int(input())
    if x==0:
        if stack:
            stack.pop()
    else:
        stack.append(x)

write(str(sum(stack)))
