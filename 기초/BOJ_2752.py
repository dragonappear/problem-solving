import sys
input = sys.stdin.readline

a,b,c = list(map(int,input().split()))
if a>=b:
    if a>=c:
        if b>=c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
else: # a<b
    if c>=b: 
        print(a,b,c)
    elif a>=c:
        print(c,a,b)
    else:
        print(a,c,b)

