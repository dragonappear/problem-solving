from sys import stdin,stdout,exit
import math
input,write=stdin.readline,stdout.write

n=int(input())

i=2
while i*i<=n:
    while True:
        if (n%i)==0: 
            write(str(i)+"\n")
            n=n//i
        else: 
            break
    i+=1

if n!=1:
    write(str(n)+"\n")