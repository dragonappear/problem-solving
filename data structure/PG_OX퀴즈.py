def solution(quiz):
    ans = []
    for q in quiz:
        exp = q.split()
        if exp[1] == '+':
            ans.append("O" if int(exp[0])+int(exp[2]) == int(exp[-1]) else "X")
        else:
            ans.append("O" if int(exp[0])-int(exp[2]) == int(exp[-1]) else "X")
    return ans
