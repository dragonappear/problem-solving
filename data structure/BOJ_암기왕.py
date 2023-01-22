# https://www.acmicpc.net/problem/2776
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

for _ in range(int(input())):
    N=int(input())
    mem=set(map(int,input().split()))
    M=int(input())
    ques=list(map(int,input().split()))
    
    for i in range(M):
        if ques[i] in mem: write("1\n")
        else: write("0\n")