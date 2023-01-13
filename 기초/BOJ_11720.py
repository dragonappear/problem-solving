import functools
n=int(input())
a=list(map(int,input()))

print(functools.reduce(lambda x,y : x+y, a))



