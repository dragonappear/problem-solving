# https://www.acmicpc.net/problem/13335
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write

N, W, L = map(int, input().split())  # 트럭 수, 다리 길이, 최대 하중
T = list(map(int, input().strip().split()))

time = 0  # 시간
tot = 0  # 무게 합
cnt = 0  # 트럭 개수
load = deque([0] * (W))
trucks = deque(T)

while True:
    if len(trucks) == 0 and tot == 0:  # 넘어갈 트럭이 없는 경우 종료
        break

    x = load.popleft()
    if x > 0:
        cnt -= 1
        tot -= x
    load.append(0)

    if trucks and tot+trucks[0] <= L and cnt+1 <= W:  # 다음에 건널수있는지 없는지
        lt = trucks.popleft()
        tot += lt
        cnt += 1
        load[-1] = lt

    time += 1

print(time)
