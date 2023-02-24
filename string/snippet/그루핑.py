import re

# grouping
# 한번 이상 반복되는 것을 찾고 싶을때
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)  # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())  # ABCABCABC

p = re.compile('ABC+')  # C만 반복되는 문자열을 찾음
m = p.search('ABCABCABC OK?')
print(m)  # <re.Match object; span=(0, 3), match='ABC'>
print(m.group())  # ABC

# 예시 1
p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m = p.search('park 010-1234-1234')
print(m.group())  # park 010-1234-1234
print(m.group(1))  # park

# 예시 2
p = re.compile(r'(\b\w+)\s+\1')
# \1 => 앞에서 걸린 문자열이 한 번더 등장할때 걸림
m = p.search('Paris in the the sping')
print(m.group())  # the the
m = p.search('Paris in the sping')
print(m)  # None


# 예시 3
# 그루핑 된 문자열에 이름 붙이기 ? P<name>
p = re.compile(r'(?P<name>\w+)\s+(?P<last>(\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group())  # park 010-1234-56789
print(m.group('name'))  # park
print(m.group('last'))  # 010-1234-56789
