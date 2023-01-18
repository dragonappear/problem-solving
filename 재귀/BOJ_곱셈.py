from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
0.5초,128MB => O(logN) or O(1)
A,B,C=[1,INT_MAX]

(a^b) mod c = ((a^(b//2)) mod c) * ((a^(b//2)) mod c) 를 활용
즉, b승은 b//2 승의 결과를 활용

1. 함수 정의
def recursive(b:int) -> a의 b승 mod c 결과를 리턴
2. Base Condition
b==1 -> a*b mod c 리턴
3. 재귀식
def recursive(b) == (recursive(b) mod c) * (recursive(b) mod c)
"""

def recursive(m:int)->int:
    if m==1: return a%c
    val = recursive(m>>1)
    val = val * val % c
    if m%2==0: return val
    else: return val*a%c

a,b,c=map(int,input().split())
write(str(recursive(b)))