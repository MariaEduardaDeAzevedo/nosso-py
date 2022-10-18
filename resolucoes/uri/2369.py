consumo = int(input())
if (consumo <= 10):
	p = 7
	print ("%d" %p)
elif (consumo > 10) and (consumo <= 30):
	p = 7 + ((consumo-10)*1)
	print ("%d" %p)
elif (consumo > 30) and (consumo <= 100):
	p1 = 27 + (2 * (consumo-30))
	print ("%d" %p1)
elif (consumo > 100):
	p2 = 167 + (5*(consumo-100))
	print ("%d" %p2)