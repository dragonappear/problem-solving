import re


s = '<html><head><title>Titile</title>'

# 그리디
print(re.match('<.*>', s).group())  # <html><head><title>Titile</title>


# 논그리디
# ? => 만족하는 패턴이 여러개 있을 때 최소한으로 매치하겠다
print(re.match('<.*?>', s).group())  # <html>
