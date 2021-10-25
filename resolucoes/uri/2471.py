n = int(input())
soma_linha = []
soma_coluna = []
matriz = []
for x in range(n):
    y = list(map(int, input().split()))
    matriz.append(y)
for z in matriz:
    a = sum(z)
    soma_linha.append(a)
for w in matriz:
    soma_coluna = [sum(x) for x in zip(*matriz)]

valores = list(set(soma_linha))
if(soma_linha.count(valores[0]) > 1):
    incorreto = valores[1]
    soma_correta = valores[0]
else:
    incorreto = valores[0]
    soma_correta = valores[1]

linha = soma_linha.index(incorreto)
coluna = soma_coluna.index(incorreto)

print(str((soma_correta - (sum(matriz[linha])- matriz[linha][coluna]))) + " " + str(matriz[linha][coluna]))
