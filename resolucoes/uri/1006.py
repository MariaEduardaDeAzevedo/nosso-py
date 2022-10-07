#Lê as informações de entrada:
A = float(input())
B = float(input())
C = float(input())

#Calcula a média ponderada:
media = (A * 2 + B * 3 + C * 5) / (2 + 3 + 5)

#Formata para 1 casa decimal:
mediaFormatada = "{:.1f}".format(media)

#Imprime o resultado:
print('MEDIA =', mediaFormatada)
