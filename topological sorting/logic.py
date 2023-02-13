
from collections import deque, defaultdict

q = deque()
deg = [0]*10  # 정점 개수가 10개 있다고 가정
N = 10
graph = defaultdict(list)  # 그래프가 이미 채워져있다고 가정

for i in range(1, N+1):
    if deg[i] == 0:  # in-degree가 0인 정점에서 출발
        q.append(i)

# O(V+E)
# 각 정점은 큐에 최대 한번 들어가고, E번만큼 indegree 감소하므로
rst = []  # 위상정렬 결과
while q:
    u = q.popleft()
    rst.append(u)
    for v in graph[u]:
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)

if len(rst) != N:  # 사이클이 존재하는 경우
    pass
else:
    print(*rst)
