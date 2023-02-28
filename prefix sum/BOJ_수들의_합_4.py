# https://www.acmicpc.net/problem/2015
from sys import stdin
from collections import defaultdict
input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
dic = defaultdict(int)

for i in range(1, N):  # 누적합 만들기
    arr[i] += arr[i-1]

ans = 0
for n in arr:
    if n == K:
        ans += 1
    # 핵심
    # O(n) 연산 대신 딕셔너리에서 찾는 것으로 시간 단축
    # 이미 본 누적합 값과 n으로 K를 만들 수 있으면 추가
    # x + n = K ->  x= n-K
    ans += dic[n-K]
    dic[n] += 1  # num을 만들 수 있는 개수 +1

print(ans)
