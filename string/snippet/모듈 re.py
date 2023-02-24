import re

# match
# 정규표현식에 일치하는 매치 객체로 반환
p = re.compile('[a-z]+')  # 괄호안에 정규표현식 지정
m = p.match('python')  # 매치 O
n = p.match('3 python')  # 매치 X
print(m)  # <re.Match object; span=(0, 6), match='python'>
print(n)  # None


# search
# 정규표현식에 일치하는 매치 객체로 반환
m = p.search('python')
n = p.search('3 3 python')
print(m)  # <re.Match object; span=(0, 6), match='python'>
print(n)  # <re.Match object; span=(4, 10), match='python'>


# findall
# 정규표현식에 일치하는 모든 문자열 리스트 반환
m = p.findall('life is too short')
print(m)  # ['life', 'is', 'too', 'short']


# finditer
# 정규표현식에 일치하는 매치 이터레이터 반환
m = p.finditer('life is too short')
print(m)  # <callable_iterator object at 0x100e1fe20>
for a in m:
    print(a)  # <re.Match object; span=(0, 4), match='life'>


"""
match 객체 메서드
.group(): 매치된 문자열을 리턴
.start(): 매치된 문자열의 시작 위치를 리턴
.end(): 매치된 문자열의 끝 위치를 리턴
.span(): 매치된 문자열의 시작,끝에 해당되는 튜플을 리턴
"""
m = p.match('python')  # 매치 O
print(m.group())  # python
print(m.start())  # 0
print(m.end())  # 6
print(m.span())  # (0, 6)
