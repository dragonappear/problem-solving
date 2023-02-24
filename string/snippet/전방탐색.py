import re

# 전방 탐색 긍정형 (?=)
p = re.compile(".+(?=:)")
m = p.search('http://google.com')
print(m.group())  # http

# 전방 탐색 부정형 (?!)
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.ext
autoexec.bat
autoexec.jpg
""")
print(l)  # ['autoexec.ext', 'autoexec.jpg']
