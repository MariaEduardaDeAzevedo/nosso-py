n,m = map(int, input().split())
abas = n
fechadas = 0
clicadas = 0
entradas = []
for x in range(m):
    entrada = input()
    entradas.append(entrada)
for y in entradas:
    if y == "fechou":
        fechadas += 1
    if y == "clicou":
        clicadas += 1
        

resultado = (abas+fechadas)-clicadas
print(resultado)
