def solution(polynomial: str):
    x = num = 0

    for n in polynomial.split(" + "):
        if n.isdigit():
            num += int(n)
        else:
            x += int(n.replace("x", "").strip()) if len(n) >= 2 else 1
    if x:
        x = str(x)+"x" if x != 1 else "x"
    else:
        x = ""

    num = str(num) if num else ""

    if x and num:
        return x + " + " + num
    elif num:
        return num
    elif x:
        return x


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
print(solution("x"))
print(solution("2x + 7"))
print(solution("1 + 1"))
