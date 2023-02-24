import re
"""
re 컴파일 옵션
DOTALL: \n 도 매치되도록 하는 옵션
IGNORECASE: 대소문자 상관없이 매치
MULTILINE: 멀티라인에서 정규 표현식 지정
VERBOSE: 긴 정규 표현식을 나눠서 쓸 수 있게 해주는 옵션
"""

# DOTALL
p = re.compile('a.b', re.DOTALL)
print(p.match('a\nb'))

# IGNORECASE
p = re.compile('[a-z]+', re.IGNORECASE)
print(p.match('ABcdEfg'))

# MULTILINE
data = """python one
life is too short
python two
you need python
python tree"""
p = re.compile('^python\s\w+', re.MULTILINE)
print(p.findall(data))  # ['python one', 'python two', 'python tree']
