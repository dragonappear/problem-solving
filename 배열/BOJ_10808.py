from collections import Counter
from sys import stdout
write = stdout.write

counter = Counter(list(input()))
arr = [ counter[chr(i)] for i in range(97,123)]
write(arr)