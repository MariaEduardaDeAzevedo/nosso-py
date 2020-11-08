n = int(input())

while (n > 0):
    st = input("")

    fin = 0
    for item in enumerate(st):
        # item (int, str) = ([0], [1])
        if (item[1] == '1'):
            fin += 2
        elif (item[1] == '2' or item[1] == '3' or item[1] == '5'):
            fin += 5
        elif (item[1] == '4'):
            fin += 4
        elif (item[1] == '6' or item[1] == '9' or item[1] == '0'):
            fin += 6
        elif (item[1] == '8'):
            fin += 7
        elif (item[1] == '7'):
            fin += 3
    print("%i leds" % fin)
    n-=1