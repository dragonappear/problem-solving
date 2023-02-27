# https://www.acmicpc.net/problem/20438
from sys import stdin
input = stdin.readline


N, K, Q, M = map(int, input().split())  # 학생 수 ,조는 수, 출석 코드 수, 구간 수
sleep = set(map(int, input().split()))
given = list(map(int, input().split()))

d = [0] * (5050)

for q in given:
    if q in sleep:
        continue

    st = q
    while st <= N+2:
        if st not in sleep:
            d[st] = 1
        st += q

psum = [0] * (5050)

for i in range(3, N+3):
    psum[i] = psum[i-1]
    if d[i] == 0:
        psum[i] += 1

for _ in range(M):
    S, E = map(int, input().split())
    print(psum[E]-psum[S-1])
