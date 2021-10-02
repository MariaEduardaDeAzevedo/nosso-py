n = int(input()) #Primeira linha pega o valor em reais

# Calcular a quantidade de notas de 100 reais
n100 = n//100
r = n%100

# Calcular a quantidade de notas de 50 reais
n50 = r//50
r = r%50

# Calcular a quantidade de notas de 20 reais
n20 = r//20
r = r%20

# Calcular a quantidade de notas de 10 reais
n10 = r//10
r = r%10

# Calcular a quantidade de notas de 5 reais
n5 = r//5
r = r%5

# Calcular a quantidade de notas de 2 reais
n2 = r//2
r = r%2

# Calcular a quantidade de notas de 1 reais
n1 = r//1
r = r%1

# Retorna tudo na saida
print(n)
print(n100,"nota(s) de R$ 100,00")
print(n50,"nota(s) de R$ 50,00")
print(n20,"nota(s) de R$ 20,00")
print(n10,"nota(s) de R$ 10,00")
print(n5,"nota(s) de R$ 5,00")
print(n2,"nota(s) de R$ 2,00")
print(n1,"nota(s) de R$ 1,00")

