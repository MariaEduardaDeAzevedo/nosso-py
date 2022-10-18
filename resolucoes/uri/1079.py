n = int(input())
ct = 1
while n >= ct:
    n1, n2, n3 = map(float, input().split())
    media = float (((n1*2)+(n2*3)+(n3*5))/10)
    print ("%.1f" %media)
    ct += 1