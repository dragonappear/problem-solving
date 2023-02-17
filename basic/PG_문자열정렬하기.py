def solution(my_string: str):
    return ''.join(map(str, sorted(list(my_string.lower()))))
