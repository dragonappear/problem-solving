import re

# 백슬래시 문제
p = re.compile(r'\\section')
# <re.Match object; span=(0, 8), match='\\section'>
print(p.match('\section'))

# 메타문자 |
p = re.compile('Crow|Servo')
print(p.match('CrowHello'))  # <re.Match object; span=(0, 4), match='Crow'>

# 메타문자 ^
# 문자열 가장 처음에 ^다음에 나오는 문자열이 나오면 매치
print(re.search('^Life', 'Life is too short'))  # 매치 (O)
# <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))  # 매치 (X)
# None

# 메타문자 $
# $전에 나오는 문자열이 나오면 매치
print(re.search('short$', 'Life is too short'))  # 매치 (O)
# <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python'))  # 매치 (X)
# None

# 메타문자 \b
# 공백을 나타내는 문자열
print(re.search(r'\bclass\b', 'no class at all'))
# <re.Match object; span=(3, 8), match='class'>
print(re.search(r'\bclass\b', 'the declassified algorithm'))
# None
print(re.search(r'\bclass\b', 'one subclass is'))
# None
