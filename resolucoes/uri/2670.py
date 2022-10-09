a=int(input())
b=int(input())
c=int(input())
a1=(b*2)+(c*4)
b1=(a*2)+(c*2)
c1=(b*2)+(a*4)
if a1<=b1 and a1<=c1:
    print(a1)
elif b1<=a1 and b1<=c1:
    print(b1)
elif c1<=a1 and c1<=b1:
    print(c1)