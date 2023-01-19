from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
연속하는 P일 중, L일동안만 사용할 수 있다. 
V = 총 휴가일
1<L<P<V
캠핑장을 최대 몇일까지 사용할수있는지
"""

i = 1
while True:
    l,p,v= map(int,input().split())

    if l==0 and p==0 and v==0:
        break
    
    write( "Case "+ str(i)+ ": " + str(v//p * l + min(v%p,l))+"\n")
    i+=1