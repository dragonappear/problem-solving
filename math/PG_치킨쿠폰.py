ans = 0


def solution(chicken):
    global ans

    if chicken >= 10:
        d, m = divmod(chicken, 10)
        ans += d
        solution(d+m)
    return ans


print(solution(1081))
