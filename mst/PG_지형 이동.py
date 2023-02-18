# https://school.programmers.co.kr/learn/courses/30/lessons/62050
def solution(land, height):

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        x = find(a)
        y = find(b)

        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    answer = 0
    N = len(land)
    dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    edges = set()

    for r in range(N):
        for c in range(N):
            for dr, dc in dr_dc:
                nr, nc = r+dr, c+dc

                if not(0 <= nr < N) or not(0 <= nc < N):
                    continue
                diff = abs(land[r][c]-land[nr][nc])
                if diff > height:
                    edges.add((diff, r*N+c, nr*N+nc))
                else:
                    edges.add((1, r*N+c, nr*N+nc))

    edges = sorted(list(edges))
    parent = [i for i in range(N*N)]

    ans = cnt = 0
    for edge in edges:
        cost, a, b = edge
        if find(a) == find(b):
            continue
        union(a, b)
        if cost > 1:
            ans += cost
        cnt += 1

        if cnt == N*N-1:
            break

    return ans


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [
      10, 10, 10, 10], [10, 10, 10, 20]], 3))
