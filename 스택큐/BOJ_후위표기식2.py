# https://www.acmicpc.net/problem/1935
import sys
from collections import defaultdict
input = sys.stdin.readline
'''
후위표기식은 인간이 사용하는 계산 표기식을 기계가 사용할수있는 표현식이며, 스택을 이용한다.
스택을 이용하여 풀이한다.
time: O(n), n=[1,26]
space: O(n), n=[1,26]
'''

n = int(input()) # n
expression = input().strip() # 후위표기식
char_map = defaultdict(int) # 문자-숫자 매핑

for i in range(n): # 문자-숫자 매핑 초기화 
    n = int(input())
    char_map[chr(65+i)] = n

    
stack = []
for char in expression: # O(n)
    if char.isalpha(): # 문자면 stack에 삽입
        stack.append(char_map[char]) 
    else: # 연산자면 연산처리 후 stack에 삽입
        right = stack.pop()
        left = stack.pop()
        result = eval(str(left) + char + str(right))
        stack.append(result)
    
print(f'{float(stack.pop()):.2f}') # 출력