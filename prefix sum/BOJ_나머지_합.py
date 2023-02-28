# https://www.acmicpc.net/problem/10986
from sys import stdin
from collections import defaultdict
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dic = defaultdict(int)
for i in range(1, N):
    arr[i] += arr[i-1]

for i in range(N):
    arr[i] %= M

ans = 0
for n in arr:
    if n == 0:
        ans += 1

    ans += dic[(n-M) % M]
    dic[n] += 1

print(ans)

# mod = [0] * 1000

# mod[0] = 1
# sum = 0  # 누적합
# for n in arr:
#     n %= M
#     sum = (sum+n) % M
#     mod[sum] += 1

# ans = 0
# for i in range(M):
#     ans += (mod[i]*(mod[i]-1)//2)

# print(ans)

"""
수열을 S 누적합의 배열을 PrefixSum이라 한다면 S[i+1]번째부터 S[j]까지의 구간합은 PrefixSum[j] - PrefixSum[i]이다.
문제에서는 (PrefixSum[j] - PrefixSum[i] ) % MOD = 0이 되는 i, j의 쌍을 구하는 것을 요구하고 있다.

모듈러 연산에 의해  

(PrefixSum[j] - PrefixSum[i] ) % MOD = 0 이 만족한다면
PrefixSum[j] % MOD = PrefixSum[i] % MOD 도 만족하게 된다.
"""
