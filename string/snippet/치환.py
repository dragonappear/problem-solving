import re

# 문자열 바꾸기
p = re.compile("(blue|white|red)")
c = p.sub('color', 'blue socks and red shoes')
print(c)  # color socks and color shoes
