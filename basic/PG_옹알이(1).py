from itertools import permutations


def solution(babbling):
    tot = []
    arr = ["aya", "ye", "woo", "ma"]
    for i in range(1, 5):
        for combi in permutations([j for j in range(4)], i):
            tmp = ""
            for a in combi:
                tmp += arr[a]
            tot.append(tmp)
    tot = set(tot)

    return sum(1 for b in babbling if b in tot)


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
