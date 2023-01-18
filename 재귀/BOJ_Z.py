from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
1초,256MB => O(N)

1. 문제 읽기
2. 논리적 순서
3. 필요한 자료연산 리스트업
4. 자료형, 시간복잡도, 유리한 자료구조 선택
5. 구현
6. 엣지케이스

n=k일때의 결과를 가지고, n=k+1의 결과를 구할수있다. => 재귀

1. 함수 정의
2. 베이스 컨디션
3. 재귀식
"""

def Z(n:int,r:int,c:int): # 1. 함수 정의 : 2^n * 2^n 배열에서 (r,c)를 방문하는 순서를 반환하는 함수
    # 2. Base condition:
    if n==0: return 0

    half = (1<<(n-1))
    if r<half and c < half: return Z(n-1,r,c) # r,c 가 1번 사각형일때
    if r<half and c >= half: return half*half + Z(n-1,r,c-half) # r,c 가 2번 사각형일때
    if r >= half and c < half: return 2*half*half + Z(n-1,r-half,c) # r,c 가 3번 사각형일때
    return 3*half*half + Z(n-1,r-half,c-half) # r,c 가 4번 사각형일때

N,r,c=map(int,input().split())
write(str(Z(N,r,c)))