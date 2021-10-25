n = int(input())
for testes in range (n):
    a = int(1)
    b = int(0)
    c = int(input())
    d = int(c**(1/2))+1
    while (a<=d):
        if (c%a==0):
            b+=1
            if (b>2):
                a = c+1
        a+=2
    if b == 1 and c > 1 :
       print ('Prime')
    else:
       print ('Not Prime') 