import sys
from collections import Counter
input = sys.stdin.readline

a =list(map(int,input().split()))

freq = Counter(a).most_common(1)
number= freq[0][0]
count = freq[0][1]


if count==3:
    print(10_000 + (number) * 1_000)
elif count==2:
    print(1_000 + (number) * 100)
else:
    print(max(a) * 100)