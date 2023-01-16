from sys import stdin,stdout
input = stdin.readline
write = stdout.write

bracket_map = {"]":"[","}":"{",")":"("}
answer = []
while True:
    s = input().rstrip()
    
    if(s=="."):
        break

    stack = []
    for c in s:
        if c in bracket_map and (not stack or stack[-1]!=bracket_map[c]):
            stack.append(False)
            break
        elif c in bracket_map and stack and stack[-1]==bracket_map[c]:
            stack.pop()
        elif c in bracket_map.values():
            stack.append(c)
    
    if stack:
        answer.append("no")
    else:
        answer.append("yes")

for a in answer:
    write(a+"\n")
            
    
