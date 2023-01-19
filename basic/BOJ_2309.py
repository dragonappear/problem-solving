import sys
input = sys.stdin.readline

dwarfs = [ int(input()) for _ in range(9)]
dwarfs.sort()
s = sum(dwarfs)

for i in range(8):
    for j in range(9):
        if s-dwarfs[i]-dwarfs[j]==100:
            for n in dwarfs:
                if n!=dwarfs[i] and n!=dwarfs[j]:
                    print(n)
            sys.exit()
