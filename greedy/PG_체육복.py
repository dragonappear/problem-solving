# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):

    nreserve = set(reserve).difference(set(lost))
    nlost = set(lost).difference(set(reserve))

    for r in nreserve:
        front = r-1
        back = r+1

        if front in nlost:
            nlost.remove(front)
        elif back in nlost:
            nlost.remove(back)

    return n-len(nlost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(5, [2, 4], [2]))
