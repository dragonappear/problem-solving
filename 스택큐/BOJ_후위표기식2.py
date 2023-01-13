# https://www.acmicpc.net/problem/1935
import sys
from collections import defaultdict
input = sys.stdin.readline
'''
1. 문제 읽기
2. 논리적 순서
3. 필요한 자료연산 리스트업
4. 자료형, 시간복잡도, 유리한 자료구조 선택
5. 구현
6. 엣지케이스
'''

# time: O(n), n is the number of letters
# space: O(n), n is length of letters
if __name__=="__main__":
    
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