n = int(input())

for i in range(1,n+1):
    left = ' '*(n-i)
    right = '*'*(i)
    print(left+right)

for i in range(1,n):
    left = ' '*(i)
    right = '*'*(n-i)
    print(left+right)

