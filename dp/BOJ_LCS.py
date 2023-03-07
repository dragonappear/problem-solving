# https://www.acmicpc.net/problem/9251
# https://kbw1101.tistory.com/25
from sys import stdin
input = stdin.readline

s1 = input().strip()
s2 = input().strip()

d = [[0]*1005 for _ in range(1005)]

"""
1. 테이블 정의: d[i][j]: s1의 (i-1)번째 문자와 s2의 (j-1)번째 문자까지 최장 공통 부분 수열의 길이
"""

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[len(s1)][len(s2)])
