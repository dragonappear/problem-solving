# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
def solution(name):

    ans = 0
    mn = len(name) - 1

    for idx, alpha in enumerate(name):
        ans += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)

        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽 시작 방식
        mn = min([mn, (idx + idx + (len(name) - next)),
                  (idx + 2 * (len(name) - next))])

    ans += mn
    return ans


print(solution("JEROEN"))
print(solution("JAN"))
