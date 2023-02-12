# https://www.acmicpc.net/problem/13913
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write

MAX = 100_001
N, K = map(int, input().split())
prev = [-1]*(MAX)
q = deque([(N, 0)])
prev[N] = N

while q:
    u, t = q.popleft()
    if u == K:
        ans = t
        break

    for du in [u-1, u+1, 2*u]:
        if not(0 <= du < MAX) or prev[du] != -1:
            continue
        prev[du] = u
        q.append((du, t+1))

print(ans)
trace = []
tmp = K
while tmp != N:
    trace.append(tmp)
    tmp = prev[tmp]
trace.append(N)
print(' '.join(map(str, trace[::-1])))
