from collections import Counter
from sys import stdout
write = stdout.write

a,b,c = int(input()),int(input()),int(input())
result = Counter(str(a*b*c))

for c in list( chr(i) for i in range(48,58)):
    write(str(result[c]) + "\n")
