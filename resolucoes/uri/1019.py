v = int(input()) # Entrada de valor

#Calculado em horas
h = v//3600 
r = v%3600

#Calculado em minutos 
m = r//60

#Calculado em segundos
s = r%60

#Formatando a saida em  horas, minutos e segundos
print("{}:{}:{}".format(h,m,s))
