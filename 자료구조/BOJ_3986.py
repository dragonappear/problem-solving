from sys import stdin,stdout
input = stdin.readline
write = stdout.write

count = 0
for i in range(int(input())):
    stack = []
    flag = True
    for c in input().strip():
        if not stack: 
            stack.append(c)
        else:
            if stack[-1]==c: 
                stack.pop()
            else:
                stack.append(c)

    if stack:
        flag = False
    
    if flag==True:
        count += 1

write(str(count))