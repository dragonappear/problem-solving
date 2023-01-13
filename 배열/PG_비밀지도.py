# arr1,arr2 zip으로 묶은 후
# 각각의 원소에 대해 | 연산하면 이진수 결과가 나옴
# 이진수 결과를 # 공백으로 변환 후 리턴변수에 추가
# time: O(n^2) n=[1,16]
# space: O(n) n=[1,16]
def solution(n, arr1, arr2):
    answer = []
    char_map = {"1":"#","0":" "}
    for a,b in list(zip(arr1,arr2)):
        bi = bin(a|b)[2:].rjust(n,'0')
        answer.append(''.join([ char_map[c] for c in bi]))
    return answer

n = 6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))