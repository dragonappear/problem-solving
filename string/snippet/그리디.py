import re


s = '<html><head><title>Titile</title>'

# 그리디
print(re.match('<.*>', s).group())  # <html><head><title>Titile</title>


# 논그리디
print(re.match('<.*?>', s).group())  # <html>
