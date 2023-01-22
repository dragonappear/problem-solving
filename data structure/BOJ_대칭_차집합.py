# https://www.acmicpc.net/problem/1269
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))

print(len(A.symmetric_difference(B)))
