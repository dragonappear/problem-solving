# https://www.acmicpc.net/problem/10799
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
()=레이저
(=스택에 삽입, )=스택에서 추출
1. if prev==( : 레이저 이므로 현재 스택에 있는 원소 개수 더하기
2. else: 막대기 끝 +1

time: O(n^2)
space: O(n)
"""
stack = []
s = input()
prev = ""
count = stack_count =0
for char in s:
    if char=="(":
        stack.append(char)
        stack_count+=1
    elif char==")":
        if prev=="(":
            stack.pop()
            stack_count-=1
            count+=stack_count
        else:
            stack.pop()
            stack_count-=1
            count+=1
    prev = char

write(str(count))