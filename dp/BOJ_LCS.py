# https://www.acmicpc.net/problem/9251
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

A=input().strip()
B=input().strip()
d= [[0]*1_005 for _ in range(1_005)]
# d[i][j]= a의 i-1번째 글자와 b의 j-1번째 글자까지 최장 공통 부분 수열 길이
# 최장 공통 부분 수열을 보존하기 위해 2중 for문 사용
# d[i][j] -> if(a[i-1]==b[j-1]) d[i-1][j-1]+1
# d[i][j] -> if(a[i-1]!=b[j-1]) max(d[i-1][j],d[i][j-1])
# 초기값은 d[1][1]에 a[0]과 b[0]이 같을떄와 다를때 각각 다른 값을 저장

len_a=len(A)
len_b=len(B)

for i in range(1,len_a+1):
    for j in range(1,len_b+1):
        if (A[i-1]==B[j-1]): d[i][j]=d[i-1][j-1]+1
        else: d[i][j]=max(d[i-1][j],d[i][j-1])
            
print(d[len_a][len_b])